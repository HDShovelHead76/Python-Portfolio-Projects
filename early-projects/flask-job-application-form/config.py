import os

class Config:
    # MySQL (PyMySQL)
    DB_HOST = "localhost"
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = "udemy_flask"

    # Gmail SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USERNAME = os.getenv("GMAIL_USER")   # your gmail address
    MAIL_PASSWORD = os.getenv("GMAIL_PASS")   # your app password in .zshrc
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_TO = os.getenv("EMPLOYER_EMAIL")     # employer's email
