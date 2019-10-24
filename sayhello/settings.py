import os

from sayhello import app

dev_db = 'mysql://root:147896325@localhost:3306/sayhello'
SECRET_KEY = os.getenv('SECRET KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
