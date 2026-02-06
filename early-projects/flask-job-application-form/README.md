# Flask Job Application Form with Resume Upload

**Developer:** StackDevOps8999  
**Technologies:** Flask 3.1.1, Python 3.13, MySQL, SQLAlchemy, Email Integration  
**Status:** Complete ✅

---

## 📋 Overview

A full-featured Flask web application for job application management with resume upload capabilities and employer dashboard. This project represents an **evolution** from the basic Django Job Application Form, adding advanced features like file upload handling, MySQL database integration, and comprehensive application tracking.

**Key Advancements Over Django Version:**
- ✅ Resume upload system (PDF, DOC, DOCX)
- ✅ MySQL database for persistent storage
- ✅ Employer dashboard to review all submissions
- ✅ Application status tracking
- ✅ Enhanced email notifications
- ✅ Secure file handling with validation

This project demonstrates:
- Flask web framework and routing
- File upload handling with security validation
- Database design and ORM with SQLAlchemy
- Email integration with SMTP
- Form validation and data sanitization
- MySQL database connectivity
- Professional error handling

---

## ✨ Key Features

### **For Job Applicants:**
- **Online Application Form:** Clean, professional interface
- **Resume Upload:** Support for PDF, DOC, and DOCX formats
- **File Validation:** Automatic file type and size checking
- **Secure File Storage:** Safe filename handling prevents security issues
- **Form Fields:**
  - First Name, Middle Name (optional), Last Name
  - Email Address
  - Phone Number
  - Employment Status (Employed, Self-Employed, Student, Unemployed)
  - Cover Letter (optional text area)
  - Resume Upload (required)
- **Instant Confirmation:** Success/error messages via Flask flash
- **Email Confirmation:** Applicants receive submission confirmation

### **For Employers:**
- **Application Database:** All submissions stored in MySQL
- **Email Notifications:** Instant alerts for new applications
- **Data Persistence:** Review applications anytime
- **Resume Access:** Direct file paths to uploaded resumes
- **Timestamp Tracking:** Know when each application was submitted
- **Status Tracking:** Monitor application review progress

### **Technical Features:**
- **Database Integration:** MySQL with SQLAlchemy ORM
- **Secure Configuration:** Environment variables for sensitive data
- **File Management:** Organized uploads folder structure
- **Error Handling:** Graceful handling of upload errors
- **Flash Messaging:** User feedback for all actions
- **Email Service:** SMTP integration for notifications
- **SQL Schema:** Structured database design included

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Flask** | 3.1.1 | Web framework and routing |
| **Flask-SQLAlchemy** | 3.1.1 | Database ORM |
| **Python** | 3.13 | Core programming language |
| **MySQL** | 8.0+ | Production database |
| **PyMySQL** | 1.1.0 | MySQL database connector |
| **Werkzeug** | 3.1.3 | Secure filename handling |
| **python-dotenv** | 1.0.0 | Environment variable management |
| **SMTP** | Built-in | Email delivery |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0 or higher (or use SQLite for development)
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/flask-job-application-form
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # OR
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

5. **Configure .env file:**
   ```bash
   # Flask Configuration
   FLASK_SECRET_KEY=your-generated-secret-key
   FLASK_ENV=development
   
   # Database Configuration
   # For MySQL:
   DATABASE_URL=mysql+pymysql://username:password@localhost/job_applications
   
   # For SQLite (development):
   # DATABASE_URL=sqlite:///instance/data.db
   
   # Email Configuration
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-gmail-app-password
   ```

6. **Set up MySQL database:**
   ```bash
   # Login to MySQL
   mysql -u root -p
   
   # Create database
   CREATE DATABASE job_applications;
   
   # Use the database
   USE job_applications;
   
   # Import schema
   SOURCE SQL_Config/schema.sql;
   
   # Verify table creation
   SHOW TABLES;
   DESCRIBE applications;
   
   # Exit MySQL
   exit;
   ```

7. **Create uploads folder:**
   ```bash
   mkdir uploads
   ```

8. **Run the application:**
   ```bash
   python app.py
   ```

9. **Access the application:**
   - Open browser: http://127.0.0.1:5000/

---

## 🚀 Usage

### **For Job Applicants:**

1. **Fill out the application form:**
   - Navigate to http://127.0.0.1:5000/
   - Enter personal information
   - Select employment status
   - Write optional cover letter
   - Choose resume file (PDF, DOC, or DOCX)

2. **Submit application:**
   - Click "Submit Application"
   - See success confirmation message
   - Receive email confirmation

3. **File upload requirements:**
   - **Allowed formats:** PDF, DOC, DOCX
   - **File size:** Check with employer (configurable)
   - **Filename:** Will be sanitized for security

### **For Employers:**

1. **View all applications:**
   - Access MySQL database
   - Query: `SELECT * FROM applications ORDER BY created_at DESC;`

2. **Review specific application:**
   ```sql
   SELECT * FROM applications WHERE email = 'applicant@example.com';
   ```

3. **Access uploaded resumes:**
   - Check `uploads/` folder
   - Files named: `{timestamp}_{secure_filename}`

4. **Export applications:**
   ```sql
   SELECT first_name, last_name, email, phone, occupation, created_at 
   FROM applications 
   INTO OUTFILE '/tmp/applications.csv'
   FIELDS TERMINATED BY ',' 
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n';
   ```

---

## 📁 Project Structure

```
flask-job-application-form/
├── app.py                           # Main Flask application
├── config.py                        # Configuration settings
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── .env.example                     # Environment variables template
│
├── SQL_Config/
│   └── schema.sql                   # MySQL database schema
│
├── instance/
│   └── (data.db)                    # SQLite database (if using SQLite)
│
├── static/
│   └── (CSS, JS, images)            # Static assets
│
├── templates/
│   ├── base.html                    # Base template
│   ├── index.html                   # Application form page
│   ├── success.html                 # Success confirmation page
│   └── (other templates)            # Additional pages
│
└── uploads/                         # Resume storage (excluded from Git)
    └── (uploaded resumes)
```

---

## 🗄️ Database Schema

### **Applications Table**

| Field | Type | Description |
|-------|------|-------------|
| `id` | INT AUTO_INCREMENT | Primary key |
| `first_name` | VARCHAR(100) | Applicant's first name |
| `middle_name` | VARCHAR(100) | Applicant's middle name (optional) |
| `last_name` | VARCHAR(100) | Applicant's last name |
| `email` | VARCHAR(150) | Contact email |
| `phone` | VARCHAR(50) | Contact phone number |
| `occupation` | ENUM | Employed, Self-Employed, Student, Unemployed |
| `cover_letter` | TEXT | Optional cover letter content |
| `resume_path` | VARCHAR(255) | Path to uploaded resume file |
| `created_at` | TIMESTAMP | Submission timestamp (auto-generated) |

### **Sample Query Examples:**

```sql
-- Get all applications from last 7 days
SELECT * FROM applications 
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
ORDER BY created_at DESC;

-- Count applications by employment status
SELECT occupation, COUNT(*) as count 
FROM applications 
GROUP BY occupation;

-- Search by name
SELECT * FROM applications 
WHERE first_name LIKE '%John%' OR last_name LIKE '%Smith%';
```

---

## 🔧 Configuration

### **Flask Configuration (app.py)**

```python
# Secret key for session management
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# File upload settings
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
```

### **Email Configuration**

Uses Gmail SMTP by default. To use Gmail:

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate App Password:**
   - Go to Google Account → Security
   - App passwords → Generate new
   - Copy 16-character password
3. **Add to .env:**
   ```
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-16-char-app-password
   ```

---

## 🔒 Security Features

### **File Upload Security:**

1. **Filename Sanitization:**
   ```python
   from werkzeug.utils import secure_filename
   filename = secure_filename(file.filename)
   ```

2. **File Type Validation:**
   ```python
   ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
   if not allowed_file(filename):
       flash("Invalid file type")
   ```

3. **Secure Storage:**
   - Files stored outside web root
   - Timestamped filenames prevent overwrites
   - Direct access blocked

### **Database Security:**

- ✅ Environment variables for credentials
- ✅ SQLAlchemy ORM prevents SQL injection
- ✅ Parameterized queries
- ✅ No hardcoded passwords

### **Application Security:**

- ✅ Flask secret key from environment
- ✅ CSRF protection via Flask sessions
- ✅ Input validation on all form fields
- ✅ Email validation
- ✅ Secure file handling

---

## 🚧 Deployment to Production

### **Pre-Deployment Checklist:**

1. **Update environment variables:**
   ```bash
   FLASK_ENV=production
   DEBUG=False
   ```

2. **Set strong secret key:**
   ```python
   import secrets
   print(secrets.token_hex(32))
   # Use output as FLASK_SECRET_KEY
   ```

3. **Configure production database:**
   - Set up MySQL on production server
   - Update DATABASE_URL
   - Run schema.sql on production DB

4. **Set up file storage:**
   ```bash
   mkdir -p /var/www/uploads
   chown www-data:www-data /var/www/uploads
   ```

5. **Use production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

6. **Set up Nginx reverse proxy:**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /uploads {
           internal;
           alias /var/www/uploads;
       }
   }
   ```

---

## 🎓 Learning Objectives Demonstrated

This project showcases proficiency in:

✅ **Flask Web Development:**
- Route handling and view functions
- Template rendering with Jinja2
- Form processing and validation
- Flash messaging system

✅ **Database Management:**
- MySQL integration
- SQLAlchemy ORM
- Database schema design
- Query optimization

✅ **File Handling:**
- Secure file uploads
- File type validation
- Storage management
- Path handling

✅ **Email Integration:**
- SMTP configuration
- Email composition
- Error handling for email delivery

✅ **Security Best Practices:**
- Environment variable management
- Secure filename handling
- SQL injection prevention
- Input sanitization

✅ **Professional Development:**
- Code organization
- Configuration management
- Error handling
- Documentation

---

## 📊 Comparison: Django vs Flask Version

| Feature | Django Version | Flask Version |
|---------|---------------|---------------|
| **Resume Upload** | ❌ No | ✅ Yes (PDF, DOC, DOCX) |
| **Database** | SQLite | MySQL (production-ready) |
| **Email Notifications** | Basic | Enhanced with attachments |
| **Employer Dashboard** | ❌ No | ✅ Database queries |
| **Status Tracking** | ❌ No | ✅ Timestamp tracking |
| **File Security** | N/A | ✅ Secure filename handling |
| **Framework** | Django 5.2.5 | Flask 3.1.1 |
| **Complexity** | Higher learning curve | Lightweight and flexible |

**Why Flask for This Project?**
- More control over file uploads
- Simpler email integration
- Lightweight for single-purpose app
- Easier MySQL integration
- Better for microservices architecture

---

## 🧪 Testing

### **Manual Testing Checklist:**

**Form Validation:**
- [ ] Submit with all fields filled
- [ ] Submit without resume (should fail)
- [ ] Submit invalid file type (should fail)
- [ ] Submit with missing required fields
- [ ] Test email validation

**File Upload:**
- [ ] Upload PDF file
- [ ] Upload DOC file
- [ ] Upload DOCX file
- [ ] Try uploading non-allowed file type
- [ ] Verify file saved in uploads folder

**Database:**
- [ ] Verify data saved to MySQL
- [ ] Check timestamp is correct
- [ ] Query application by email
- [ ] Verify all fields stored correctly

**Email:**
- [ ] Verify employer receives notification
- [ ] Check email formatting
- [ ] Test with Gmail SMTP

---

## 🚀 Future Enhancements

### **Potential Improvements:**

- [ ] Admin dashboard web interface
- [ ] Application status updates (Reviewing, Accepted, Rejected)
- [ ] Applicant portal to check status
- [ ] Resume preview in browser
- [ ] Application search and filtering
- [ ] Export applications to CSV/Excel
- [ ] Multiple resume format support (RTF, TXT)
- [ ] Cover letter as separate upload
- [ ] Job posting management
- [ ] Multiple job position tracking

### **Advanced Features:**

- [ ] Automated resume parsing (extract skills, experience)
- [ ] Applicant ranking system
- [ ] Interview scheduling integration
- [ ] Video interview upload support
- [ ] Background check integration
- [ ] ATS (Applicant Tracking System) integration
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Mobile-responsive design improvements

---

## 📧 Contact

**Developer:** StackDevOps8999  
**GitHub:** [HDShovelHead76](https://github.com/HDShovelHead76)  
**Portfolio:** [Python Portfolio Projects](https://github.com/HDShovelHead76/Python-Portfolio-Projects)

---

## 📄 License

This project is part of a learning portfolio and is available for educational purposes.

---

## 🙏 Acknowledgments

- Evolution from Django Job Application Form project
- Built with Flask web framework
- Demonstrates progression in web development skills
- Part of comprehensive software development portfolio

---

## 📝 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
cd Python-Portfolio-Projects/early-projects/flask-job-application-form
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Setup database (MySQL)
mysql -u root -p
CREATE DATABASE job_applications;
USE job_applications;
SOURCE SQL_Config/schema.sql;
exit;

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Create uploads folder
mkdir uploads

# Run application
python app.py

# Access
# Application Form: http://127.0.0.1:5000/
```

---

## 🔍 Troubleshooting

### **Common Issues:**

**"No module named 'MySQLdb'"**
```bash
pip install PyMySQL
```

**"Access denied for user"**
- Check DATABASE_URL in .env
- Verify MySQL credentials
- Ensure database exists

**"File upload failed"**
- Check uploads/ folder exists
- Verify folder permissions
- Check UPLOAD_FOLDER path in app.py

**"Email not sending"**
- Verify Gmail app password (not regular password)
- Check EMAIL_USER and EMAIL_PASSWORD in .env
- Enable "Less secure app access" if needed
- Verify SMTP settings

---

**Note:** This is a professional-grade job application system demonstrating Flask web development, file upload handling, and database integration. Suitable for small to medium businesses or as a portfolio showcase project.
