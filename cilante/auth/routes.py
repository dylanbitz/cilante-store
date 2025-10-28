from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm
from ..models import Usuarios
from . import auth
from ..models import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login exitoso.', 'success')
            return redirect(url_for('shop.index'))  # Redirigir a la página principal de la tienda
        flash('Correo o contraseña incorrectos.', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = Usuarios()
        new_user.email = form.email.data
        new_user.username = form.username.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)