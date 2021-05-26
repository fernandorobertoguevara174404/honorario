from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,SubmitField
from wtforms.validators import DataRequired

class Calculo(FlaskForm):
    valor = FloatField('Introduzca honorarios', validators=[DataRequired(message='El número introducido es incorrecto')])
    submit = SubmitField('Calcular totales')