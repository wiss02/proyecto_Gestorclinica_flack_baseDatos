from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
login_manager.login_message_category = 'warning'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.models.usuario import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Registrar blueprints
    from app.controllers.main_controller import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.medico_controller import medico_bp
    from app.controllers.paciente_controller import paciente_bp
    from app.controllers.consulta_controller import consulta_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(medico_bp, url_prefix='/medicos')
    app.register_blueprint(paciente_bp, url_prefix='/pacientes')
    app.register_blueprint(consulta_bp, url_prefix='/consultas')

    return app
