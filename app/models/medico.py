from app import db


class Medico(db.Model):
    __tablename__ = 'medicos'

    id_medico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(120), nullable=False, unique=True)

    # Relación: un médico tiene muchas consultas
    consultas = db.relationship('Consulta', backref='medico', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Medico {self.nombre} - {self.especialidad}>'
