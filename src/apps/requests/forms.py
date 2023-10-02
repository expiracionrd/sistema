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
]

choices_state=[
    ("pendiente", "Pendiente"),
    ("proceso", "Proceso"),
    ("completadas", "Completadas")
    
]



class RequestsForm(FlaskForm):    
    name = fields.StringField(label="Nombre", validators=[DataRequired("Este campo es requerido"), Length(max=60, message="No debe de tener mas de 60 caracteres")],  )
    
    mount = fields.IntegerField(label="Monto", 
        validators=[
            DataRequired("Este campo es requerido"), 
            NumberRange(min=1, message="El capital solicitado no puede ser menor o igual a cero.")
        ] 
    )
    
    reason = fields.TextAreaField(
        label="Motivo de la solicitud"
    )
    
    discount = fields.SelectField(
        label="Forma de pago", 
        validators=[
            DataRequired("Este campo es requerido")
        ],
        choices=choices_discount
    )
    
    deadlines = fields.SelectField(
        label="Plazos o cantidad de cuotas", 
        validators=[
            DataRequired("Este campo es requerido")
        ], 
        choices=choices_deadline_data()
    )
    
    location = fields.SelectField(
        label="Territorio", 
        validators=[
            DataRequired("Este campo es requerido")
        ], 
        choices=choices_location
    )