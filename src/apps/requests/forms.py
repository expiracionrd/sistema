from src.extensions.db import db
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Length, NumberRange


choices_discount = [
    ("Quincenal", "Quincenal"),
    ("Mensual", "Mensual"),
    ("Comisión", "Comisión")
]


def choices_deadline_data():
    choices_deadline = []
    
    for i in range(1, 73):
        choices_deadline.append(i)
    
    return choices_deadline

choices_location = [
    ("Norte", "Norte"),
    ("Sur", "Sur"),
    ("Este", "Este"),
    ("Oeste", "Oeste")
]

choices_state=[
    ("Pendiente", "Pendiente"),
    ("Trabajada", "Trabajada"),
    ("Completadas", "Completadas")
    
]



class RequestsForm(FlaskForm):    
    name = fields.StringField(label="Nombre", validators=[DataRequired("Este campo es requerido"), Length(max=60, message="No debe de tener mas de 60 caracteres")],  )
    
    mount = fields.IntegerField(label="Monto", 
        validators=[
            DataRequired("Este campo es requerido"), 
            NumberRange(min=1, message="El Monto no puede ser negativo ni igual a cero")
        ] 
    )
    
    reason = fields.TextAreaField(
        label="Motivo de la solicitud"
    )
    
    discount = fields.SelectField(
        label="Descuento", 
        validators=[
            DataRequired("Este campo es requerido")
        ],
        choices=choices_discount
    )
    
    deadlines = fields.SelectField(
        label="Cuotas", 
        validators=[
            DataRequired("Este campo es requerido")
        ], 
        choices=choices_deadline_data()
    )
    
    location = fields.SelectField(
        label="Ubicacion", 
        validators=[
            DataRequired("Este campo es requerido")
        ], 
        choices=choices_location
    )