from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app import db
from app.models.medico import Medico

medico_bp = Blueprint('medicos', __name__, template_folder='../templates')


@medico_bp.route('/')
@login_required
def index():
    medicos = Medico.query.order_by(Medico.nombre).all()
    return render_template('medicos/index.html', medicos=medicos)


@medico_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        especialidad = request.form.get('especialidad', '').strip()
        telefono = request.form.get('telefono', '').strip()
        correo = request.form.get('correo', '').strip()

        if not nombre or not especialidad or not telefono or not correo:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('medicos/create.html')

        if Medico.query.filter_by(correo=correo).first():
            flash('Ya existe un médico con ese correo.', 'danger')
            return render_template('medicos/create.html')

        medico = Medico(nombre=nombre, especialidad=especialidad,
                        telefono=telefono, correo=correo)
        db.session.add(medico)
        db.session.commit()

        flash('Médico registrado exitosamente.', 'success')
        return redirect(url_for('medicos.index'))

    return render_template('medicos/create.html')


@medico_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    medico = Medico.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        especialidad = request.form.get('especialidad', '').strip()
        telefono = request.form.get('telefono', '').strip()
        correo = request.form.get('correo', '').strip()

        if not nombre or not especialidad or not telefono or not correo:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('medicos/edit.html', medico=medico)

        existente = Medico.query.filter_by(correo=correo).first()
        if existente and existente.id_medico != medico.id_medico:
            flash('Ya existe otro médico con ese correo.', 'danger')
            return render_template('medicos/edit.html', medico=medico)

        medico.nombre = nombre
        medico.especialidad = especialidad
        medico.telefono = telefono
        medico.correo = correo
        db.session.commit()

        flash('Médico actualizado exitosamente.', 'success')
        return redirect(url_for('medicos.index'))

    return render_template('medicos/edit.html', medico=medico)


@medico_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def delete(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    flash('Médico eliminado exitosamente.', 'success')
    return redirect(url_for('medicos.index'))
