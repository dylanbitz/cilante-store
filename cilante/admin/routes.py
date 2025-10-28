from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from cilante.models import Usuarios
from . import admin

@admin.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@admin.route('/admin/users')
@login_required
def manage_users():
    users = Usuarios.query.all()
    return render_template('admin/manage_users.html', users=users)

@admin.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = Usuarios.query.get_or_404(user_id)
    # Logic to delete the user
    # db.session.delete(user)
    # db.session.commit()
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin.manage_users'))

@admin.route('/admin_under_construction')
def admin_under_construction():
    return "Esta pagina todavia está en construcción."