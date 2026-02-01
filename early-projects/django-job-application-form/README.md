# Django Job Application Form

A Django web application demonstrating form handling, data validation, and automated email notifications. Built as a learning project to practice core Django concepts including models, forms, views, and email integration.

## 📋 Description

This project implements a simple job application form that collects basic applicant information and sends automated email notifications to the employer. The application showcases fundamental Django development skills including:

- Form creation and validation using Django Forms
- Model-based data persistence with SQLite
- Email integration using Django's email framework
- Bootstrap-based responsive UI
- Template inheritance and URL routing
- Environment-based configuration using `.env` files

**Key Features:**
- Clean, responsive Bootstrap interface
- Real-time form validation
- Automated email notifications to employer
- Database storage of all applications
- Environment variable configuration for security

## 🎯 Learning Objectives

This project demonstrates proficiency in:
- Django MVT (Model-View-Template) architecture
- Django Forms framework
- Django ORM and database migrations
- Email configuration and SMTP integration
- Environment-based configuration management
- Bootstrap integration for responsive design
- Secure credential handling

## 🛠️ Technologies

- **Framework:** Django 5.2.5
- **Frontend:** HTML5, Bootstrap 5.1.3, jQuery
- **Database:** SQLite3
- **Email:** SMTP with Gmail
- **Configuration:** python-dotenv for environment variables

## 📋 Form Fields

The application collects the following information:
- First Name
- Middle Name
- Last Name
- Email Address
- Phone Number
- Current Employment Status (Employed/Unemployed/Self-Employed/Student)

## 🚀 Installation & Setup

### Prerequisites
```bash
python --version  # Should be 3.8 or higher
```

### Setup Instructions

1. **Clone or navigate to this project:**
```bash
cd django-job-application-form
```

2. **Create a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
DJANGO_SECRET_KEY=your-unique-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
EMPLOYER_EMAIL=employer-email@example.com
```

**Note:** For Gmail, you'll need to generate an [App Password](https://support.google.com/accounts/answer/185833).

5. **Run database migrations:**
```bash
python manage.py migrate
```

6. **Create a superuser (optional, for admin access):**
```bash
python manage.py createsuperuser
```

7. **Run the development server:**
```bash
python manage.py runserver
```

8. **Access the application:**
- Application: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure
```
django-job-application-form/
├── job_application/        # Main application
│   ├── models.py          # Form data model
│   ├── forms.py           # Django form definition
│   ├── views.py           # View logic and email handling
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── mysite/                # Project configuration
│   ├── settings.py        # Django settings (uses .env)
│   └── urls.py            # Root URL configuration
├── templates/             # Base templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── .gitignore            # Git ignore rules
```

## 💡 How It Works

1. **User visits the home page** and fills out the job application form
2. **Django validates** the form data on the server side
3. **On successful submission:**
   - Application data is saved to the SQLite database
   - An automated email is sent to the employer with application details
   - User sees a success confirmation message
4. **Employer receives** formatted email with applicant information

## 🧪 Testing Email Functionality

A standalone email test script is included:
```bash
python email_test.py
```

This verifies your SMTP configuration without running the full application.

## 🔒 Security Notes

- **Never commit `.env` files** to version control
- Use environment variables for all sensitive data
- Generate unique Django secret keys for each deployment
- Use Gmail App Passwords, not your actual Gmail password
- Set `DEBUG=False` in production environments

## 🔮 Future Enhancements

Potential improvements for this project:
- [ ] Add resume/file upload capability
- [ ] Implement reCAPTCHA for spam prevention
- [ ] Add email confirmation to applicants
- [ ] Create applicant dashboard to track submissions
- [ ] Add more detailed employment history fields
- [ ] Implement PDF generation for applications
- [ ] Add unit and integration tests

## 📝 Notes

**Development Context:**
- Built as part of a Udemy Django course
- Focuses on core Django fundamentals
- Demonstrates secure credential management
- Uses Bootstrap for quick, responsive styling

**Key Challenges Overcome:**
- Configured Django email backend with Gmail SMTP
- Implemented environment-based configuration
- Integrated Bootstrap with Django templates
- Handled form validation and error messaging

## 📄 License

This project is part of the [Python-Portfolio-Projects](../../) repository.  
Licensed under the MIT License.

---

**Author:** StackDevOps8999  
**GitHub:** [@HDShovelHead76](https://github.com/HDShovelHead76)  
**Date:** February 2026  
**Learning Source:** Udemy Django Course
