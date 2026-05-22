from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app import db
from app.models.paciente import Paciente

paciente_bp = Blueprint('pacientes', __name__, template_folder='../templates')


@paciente_bp.route('/')
@login_required
def index():
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    return render_template('pacientes/index.html', pacientes=pacientes)


@paciente_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        edad = request.form.get('edad', '').strip()
        direccion = request.form.get('direccion', '').strip()
        telefono = request.form.get('telefono', '').strip()

        if not nombre or not edad or not direccion or not telefono:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('pacientes/create.html')

        try:
            edad = int(edad)
            if edad < 0 or edad > 150:
                raise ValueError
        except ValueError:
            flash('La edad debe ser un número válido entre 0 y 150.', 'danger')
            return render_template('pacientes/create.html')

        paciente = Paciente(nombre=nombre, edad=edad,
                            direccion=direccion, telefono=telefono)
        db.session.add(paciente)
        db.session.commit()

        flash('Paciente registrado exitosamente.', 'success')
        return redirect(url_for('pacientes.index'))

    return render_template('pacientes/create.html')


@paciente_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        edad = request.form.get('edad', '').strip()
        direccion = request.form.get('direccion', '').strip()
        telefono = request.form.get('telefono', '').strip()

        if not nombre or not edad or not direccion or not telefono:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('pacientes/edit.html', paciente=paciente)

        try:
            edad = int(edad)
            if edad < 0 or edad > 150:
                raise ValueError
        except ValueError:
            flash('La edad debe ser un número válido entre 0 y 150.', 'danger')
            return render_template('pacientes/edit.html', paciente=paciente)

        paciente.nombre = nombre
        paciente.edad = edad
        paciente.direccion = direccion
        paciente.telefono = telefono
        db.session.commit()

        flash('Paciente actualizado exitosamente.', 'success')
        return redirect(url_for('pacientes.index'))

    return render_template('pacientes/edit.html', paciente=paciente)


@paciente_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def delete(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado exitosamente.', 'success')
    return redirect(url_for('pacientes.index'))
