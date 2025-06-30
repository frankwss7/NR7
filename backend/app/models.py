# backend/app/models.py

from . import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.email}>"
