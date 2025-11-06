from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Usuarios(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.user_id)

class Comentarios(db.Model):
    coment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contenido = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.user_id'), nullable=False)

class Contactos(db.Model):
    contacto_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.user_id'), nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(13), nullable=False, unique=True)

class ChatLogs(db.Model):
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conversacion_id = db.Column(db.String(64), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.user_id'), nullable=False)
    mensaje_usuario = db.Column(db.String(100), nullable=False)
    respuesta_bot = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), index=True)