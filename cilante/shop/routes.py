from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import ContactForm
from . import shop

@shop.route('/')
def index():
    return render_template('index.html')

@shop.route('/product')
def product():
    # Aquí se puede agregar la lógica para obtener información del producto
    return render_template('product.html')

@shop.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Aquí se puede agregar la lógica para enviar el formulario
        flash('Mensaje enviado con éxito', 'success')
        return redirect(url_for('shop.contact'))
    return render_template('contact.html', form=form)