import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables
EMAIL_USER = os.environ.get("GMAIL_USER")
EMAIL_PASS = os.environ.get("GMAIL_PASS")

if not EMAIL_USER or not EMAIL_PASS:
    raise RuntimeError("❌ Missing GMAIL_USER or GMAIL_PASS environment variables!")

def send_test_email():
    try:
        # Prepare email
        msg = MIMEText("This is a standalone Gmail SMTP test 🚀")
        msg["Subject"] = "Gmail Env Var Test"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER

        # Connect to Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("✅ Test email sent successfully!")

    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    send_test_email()
