from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length, ValidationError


class FilterForm(FlaskForm):
    nombre = StringField(label="Nombre", validators=[Length(min=0, max=20, message="El campo nombre como máximo 20 caracteres")])


class CreateForm(FlaskForm):
    dni = StringField(label="DNI", validators=[DataRequired(message="El campo DNI es obligatorio"),Length(min=0, max=10, message="El campo DNI como máximo 10 caracteres")])
    nombre = StringField(label="Nombre", validators=[DataRequired(message="El campo nombre es obligatorio"),Length(min=0, max=20, message="El campo nombre como máximo 20 caracteres")])
    apellidos = StringField(label="Apellidos", validators=[DataRequired(message="El campo apellidos es obligatorio"),Length(min=0, max=20, message="El campo nombre como máximo 30 caracteres")])
    imagen = FileField(label="Imagen", validators=[FileRequired(message="El campo imagen es obligatorio"),FileAllowed(['jpg', 'png'], message="Solo jpg y png")])

    # def validate_imagen(form,field):
    #     max_length = 1024
    #     if len(field.data.read()) > max_length:
    #         raise ValidationError(f"El fichero no puede ser superior a {max_length}")