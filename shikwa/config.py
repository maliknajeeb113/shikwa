import os


class Config:
    SECRET_KEY = '13032001'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'app.shikwa@gmail.com'
    MAIL_PASSWORD = 'kmdxbthmsftwlawl'
