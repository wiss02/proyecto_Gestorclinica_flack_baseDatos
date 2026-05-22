from flask import Blueprint, render_template
from flask_login import login_required
from app.models.medico import Medico
from app.models.paciente import Paciente
from app.models.consulta import Consulta

main_bp = Blueprint('main', __name__, template_folder='../templates')


@main_bp.route('/')
@login_required
def dashboard():
    total_medicos = Medico.query.count()
    total_pacientes = Paciente.query.count()
    total_consultas = Consulta.query.count()
    ultimas_consultas = Consulta.query.order_by(Consulta.fecha.desc()).limit(5).all()

    return render_template('main/dashboard.html',
                           total_medicos=total_medicos,
                           total_pacientes=total_pacientes,
                           total_consultas=total_consultas,
                           ultimas_consultas=ultimas_consultas)
