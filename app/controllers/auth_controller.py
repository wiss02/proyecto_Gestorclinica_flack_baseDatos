from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__, template_folder='../templates')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('auth/login.html')

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password):
            login_user(usuario)
            flash(f'¡Bienvenido, {usuario.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not username or not password or not confirm_password:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('auth/register.html')

        if password != confirm_password:
            flash('Las contraseñas no coinciden.', 'danger')
            return render_template('auth/register.html')

        if len(password) < 4:
            flash('La contraseña debe tener al menos 4 caracteres.', 'danger')
            return render_template('auth/register.html')

        if Usuario.query.filter_by(username=username).first():
            flash('El nombre de usuario ya está en uso.', 'danger')
            return render_template('auth/register.html')

        nuevo_usuario = Usuario(username=username)
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Cuenta creada exitosamente. Inicia sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))
