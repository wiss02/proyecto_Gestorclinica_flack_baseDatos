# 🏥 Sistema de Gestión de Clínica Médica

Aplicación web desarrollada con **Flask** y **SQLAlchemy** usando el patrón **MVC** para administrar la atención de una clínica médica.

## 📋 Características

- **CRUD completo** para Médicos, Pacientes y Consultas
- **Login y Registro de usuarios** (Extra)
- **Dashboard** con estadísticas en tiempo real
- **Validación** de campos obligatorios
- **Relaciones** entre tablas (Médico ↔ Consulta ↔ Paciente)
- **Interfaz profesional** y responsive
- **Base de datos SQLite** (sin configuración adicional)

## 🛠️ Tecnologías

- Python 3
- Flask (Framework Web)
- Flask-SQLAlchemy (ORM)
- Flask-Login (Autenticación)
- Flask-WTF (Protección CSRF)
- SQLite (Base de datos)
- Jinja2 (Templates)
- CSS personalizado (Diseño profesional)

## 📁 Estructura del Proyecto (MVC)

```
├── app/
│   ├── __init__.py              # Factory de la aplicación
│   ├── config.py                # Configuración
│   ├── models/                  # MODELO
│   │   ├── medico.py
│   │   ├── paciente.py
│   │   ├── consulta.py
│   │   └── usuario.py
│   ├── controllers/             # CONTROLADOR
│   │   ├── auth_controller.py
│   │   ├── main_controller.py
│   │   ├── medico_controller.py
│   │   ├── paciente_controller.py
│   │   └── consulta_controller.py
│   ├── templates/               # VISTA
│   │   ├── base.html
│   │   ├── auth/
│   │   ├── main/
│   │   ├── medicos/
│   │   ├── pacientes/
│   │   └── consultas/
│   └── static/
│       └── css/style.css
├── run.py                       # Punto de entrada
├── requirements.txt             # Dependencias
└── README.md
```

## 🚀 Instalación y Ejecución

### 1. Crear entorno virtual
```bash
python -m venv venv
```

### 2. Activar entorno virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python run.py
```

### 5. Abrir en el navegador
```
http://localhost:5000
```

## 📊 Base de Datos

### Tablas

| Tabla | Campos |
|-------|--------|
| **Médicos** | id_medico, nombre, especialidad, telefono, correo |
| **Pacientes** | id_paciente, nombre, edad, direccion, telefono |
| **Consultas** | id_consulta, fecha, diagnostico, tratamiento, id_medico (FK), id_paciente (FK) |
| **Usuarios** | id, username, password_hash |

### Relaciones
- Un médico puede atender muchas consultas (1:N)
- Un paciente puede tener muchas consultas (1:N)
- Cada consulta pertenece a un médico y a un paciente

## ⭐ Extra Implementado

- **Login y Registro de usuarios** con contraseñas hasheadas (Werkzeug)
- Protección de rutas (requiere autenticación)
- Modal de confirmación para eliminación de registros
