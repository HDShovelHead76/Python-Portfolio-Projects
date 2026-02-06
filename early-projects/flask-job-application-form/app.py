from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import pymysql
import smtplib
from email.message import EmailMessage
import os

# Load .zshrc or .env file
load_dotenv(os.path.expanduser("~/.zshrc"))
# ------------------- Configuration -------------------
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-in-production')

# File upload settings
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ------------------- Database Configuration -------------------
DB_USER = os.getenv("FLASK_DB_USER")
DB_PASSWORD = os.getenv("FLASK_DB_PASS")
DB_HOST = os.getenv("FLASK_DB_HOST")
DB_NAME = os.getenv("FLASK_DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ------------------- Gmail Configuration -------------------
GMAIL_USER = os.getenv("GMAIL_USER")  # your Gmail address
GMAIL_PASS = os.getenv("GMAIL_PASS")  # Gmail App Password

EMPLOYER_EMAIL = os.getenv("EMPLOYER_EMAIL", GMAIL_USER)  # default to Gmail user if not set

# ------------------- Database Model -------------------
class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    cover_letter = db.Column(db.Text)
    resume = db.Column(db.String(200), nullable=False)
    submitted_at = db.Column(db.DateTime, server_default=db.func.now())

# ------------------- Create tables -------------------
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print("❌ Could not connect to the database. Check your settings in .zshrc")
    print("Error:", e)

# ------------------- Helper Functions -------------------
def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def is_email_unique(email: str) -> bool:
    try:
        return Application.query.filter_by(email=email).first() is None
    except Exception:
        return False

def save_application(data: dict, resume_file):
    filename = secure_filename(resume_file.filename)
    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    resume_file.save(resume_path)
    app_entry = Application(
        first_name=data["first_name"],
        middle_name=data.get("middle_name", ""),
        last_name=data["last_name"],
        email=data["email"],
        phone=data["phone"],
        occupation=data["occupation"],
        cover_letter=data.get("cover_letter", ""),
        resume=filename,
    )
    db.session.add(app_entry)
    db.session.commit()
    return app_entry

def send_email(application: Application):
    """Send email to employer and optionally confirmation to applicant."""
    try:
        msg = EmailMessage()
        msg["From"] = GMAIL_USER
        msg["To"] = EMPLOYER_EMAIL
        msg["Subject"] = f"New Job Application: {application.first_name} {application.last_name}"

        body = f"""
New Job Application Received:

Name: {application.first_name} {application.middle_name} {application.last_name}
Email: {application.email}
Phone: {application.phone}
Occupation: {application.occupation}
Cover Letter: {application.cover_letter or 'N/A'}
Resume File: {application.resume}
Submitted At: {application.submitted_at}

"""
        msg.set_content(body)

        # Attach resume
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], application.resume)
        with open(resume_path, "rb") as f:
            file_data = f.read()
            file_name = application.resume
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_PASS)
            smtp.send_message(msg)

        # Optionally, send confirmation email to applicant
        confirmation = EmailMessage()
        confirmation["From"] = GMAIL_USER
        confirmation["To"] = application.email
        confirmation["Subject"] = "Application Received"
        confirmation.set_content(f"Hi {application.first_name},\n\nWe have received your application. Thank you!")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_PASS)
            smtp.send_message(confirmation)

    except Exception as e:
        print("❌ Failed to send email:", e)

# ------------------- Routes -------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_application():
    required_fields = ["first_name", "last_name", "email", "phone", "occupation"]
    form_data = {field: request.form.get(field) for field in required_fields}
    form_data["middle_name"] = request.form.get("middle_name", "")
    form_data["cover_letter"] = request.form.get("cover_letter", "")
    resume_file = request.files.get("resume")

    # ------------------- Validation -------------------
    if not all(form_data[field] for field in required_fields) or not resume_file:
        flash("Please fill in all required fields and upload a resume.")
        return redirect(url_for("home"))

    if not allowed_file(resume_file.filename):
        flash("Resume must be a PDF, DOC, or DOCX file.")
        return redirect(url_for("home"))

    if not is_email_unique(form_data["email"]):
        flash("An application with this email already exists.")
        return redirect(url_for("home"))

    # ------------------- Save Data & Send Email -------------------
    try:
        app_entry = save_application(form_data, resume_file)
        send_email(app_entry)
    except Exception as e:
        flash("❌ Could not save your application or send email. Please try again later.")
        print("Error:", e)
        return redirect(url_for("home"))

    return render_template(
        "thank_you.html",
        name=f"{form_data['first_name']} {form_data['last_name']}"
    )

@app.route("/applications")
def view_applications():
    try:
        apps = Application.query.all()
    except Exception as e:
        flash("❌ Could not fetch applications from the database.")
        print("Error:", e)
        apps = []
    return render_template("applications.html", apps=apps)

# ------------------- Main -------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
