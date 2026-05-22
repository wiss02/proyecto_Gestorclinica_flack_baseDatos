import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-clinica-medica-2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(basedir), 'clinica.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
