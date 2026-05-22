from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'
