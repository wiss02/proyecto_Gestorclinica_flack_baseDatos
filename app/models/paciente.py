from app import db


class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    # Relación: un paciente tiene muchas consultas
    consultas = db.relationship('Consulta', backref='paciente', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Paciente {self.nombre}>'
