from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ProductInquiryForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Length(max=100)])
    message = TextAreaField('Mensaje', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Enviar Consulta')

class PurchaseForm(FlaskForm):
    quantity = DecimalField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Comprar')
    
class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Length(max=100)])
    subject = StringField('Asunto', validators=[DataRequired(), Length(max=150)])
    message = TextAreaField('Mensaje', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Enviar Mensaje')