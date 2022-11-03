import os


class Config:
    SECRET_KEY = '-----' #enter a secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '-----' #enter the mail here
    MAIL_PASSWORD = '-----' #enter the password
