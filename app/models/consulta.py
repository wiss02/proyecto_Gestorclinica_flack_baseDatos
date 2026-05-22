from app import db
from datetime import date


class Consulta(db.Model):
    __tablename__ = 'consultas'

    id_consulta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    diagnostico = db.Column(db.Text, nullable=False)
    tratamiento = db.Column(db.Text, nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)

    def __repr__(self):
        return f'<Consulta {self.id_consulta} - {self.fecha}>'
