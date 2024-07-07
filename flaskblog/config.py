import os

class Config:
  SECRET_KEY= 'dc4b02aac588045ba12a8aa243aa379f'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.getenv('EMAIL_USER')
  MAIL_PASSWORD = os.getenv('EMAIL_PASS')
  