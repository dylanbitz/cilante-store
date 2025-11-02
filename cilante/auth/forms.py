from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from cilante.models import Usuarios

class RegistrationForm(FlaskForm):
    username = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = Usuarios.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ese nombre de usuario ya está en uso. Por favor elige uno diferente.')

    def validate_email(self, email):
        user = Usuarios.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ese correo electrónico ya está registrado. Por favor elige uno diferente.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')