from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length



class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[
        DataRequired(message="El Nombre de usuario es requerido"), 
        Length(max=60, message="El nombre de usuario no puede tener mas de 60 caracteres"),
        Length(min=1, message="El Nombre de usuario es requerido")
    ])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="La contraseña es requerida"), 
        Length(max=60, message="El password no puede tener mas de 60 caracteres"), 
        Length(min=8, message="La contraseña debe ser mayor a 8 caracteres") 
    ])
    confirm = PasswordField("Confirmar Contraseña", validators=[EqualTo("password", "Las contraseñas no coinciden")])