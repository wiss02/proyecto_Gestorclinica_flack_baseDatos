from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app import db
from app.models.consulta import Consulta
from app.models.medico import Medico
from app.models.paciente import Paciente
from datetime import datetime

consulta_bp = Blueprint('consultas', __name__, template_folder='../templates')


@consulta_bp.route('/')
@login_required
def index():
    consultas = Consulta.query.order_by(Consulta.fecha.desc()).all()
    return render_template('consultas/index.html', consultas=consultas)


@consulta_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def create():
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()

    if request.method == 'POST':
        fecha = request.form.get('fecha', '').strip()
        diagnostico = request.form.get('diagnostico', '').strip()
        tratamiento = request.form.get('tratamiento', '').strip()
        id_medico = request.form.get('id_medico', '').strip()
        id_paciente = request.form.get('id_paciente', '').strip()

        if not fecha or not diagnostico or not tratamiento or not id_medico or not id_paciente:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('consultas/create.html', medicos=medicos, pacientes=pacientes)

        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de fecha inválido.', 'danger')
            return render_template('consultas/create.html', medicos=medicos, pacientes=pacientes)

        consulta = Consulta(fecha=fecha_obj, diagnostico=diagnostico,
                            tratamiento=tratamiento, id_medico=int(id_medico),
                            id_paciente=int(id_paciente))
        db.session.add(consulta)
        db.session.commit()

        flash('Consulta registrada exitosamente.', 'success')
        return redirect(url_for('consultas.index'))

    return render_template('consultas/create.html', medicos=medicos, pacientes=pacientes)


@consulta_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    consulta = Consulta.query.get_or_404(id)
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()

    if request.method == 'POST':
        fecha = request.form.get('fecha', '').strip()
        diagnostico = request.form.get('diagnostico', '').strip()
        tratamiento = request.form.get('tratamiento', '').strip()
        id_medico = request.form.get('id_medico', '').strip()
        id_paciente = request.form.get('id_paciente', '').strip()

        if not fecha or not diagnostico or not tratamiento or not id_medico or not id_paciente:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('consultas/edit.html', consulta=consulta,
                                   medicos=medicos, pacientes=pacientes)

        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de fecha inválido.', 'danger')
            return render_template('consultas/edit.html', consulta=consulta,
                                   medicos=medicos, pacientes=pacientes)

        consulta.fecha = fecha_obj
        consulta.diagnostico = diagnostico
        consulta.tratamiento = tratamiento
        consulta.id_medico = int(id_medico)
        consulta.id_paciente = int(id_paciente)
        db.session.commit()

        flash('Consulta actualizada exitosamente.', 'success')
        return redirect(url_for('consultas.index'))

    return render_template('consultas/edit.html', consulta=consulta,
                           medicos=medicos, pacientes=pacientes)


@consulta_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def delete(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    flash('Consulta eliminada exitosamente.', 'success')
    return redirect(url_for('consultas.index'))
