from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError



class RegisterForm(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=20, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    passwordRepeat = PasswordField(label="Repita la contraseña", validators=[
        DataRequired(message="La repetición de la contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])

    dni = StringField(label="DNI", validators=[
        DataRequired(message="El dni es obligatorio"),
        Length(max=10, message="El dni no puede ser superior a 10 caracteres")
    ])

    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=20, message="El nombre no puede ser superior a 10 caracteres")
    ])

    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="Los apellidos son obligatorio"),
        Length(max=50, message="Los apellidos no pueden superar los 50 caracteres")
    ])

    def validate_password(form,field):

        hasDigit = False
        hasUpper = False
        hasSpecialChar = False
        for char in field.data:
            if char.isdigit():
                hasDigit = True
            if char.isupper():
                hasUpper = True
            if not char.isalnum():
                hasSpecialChar = True

        if not hasUpper or not hasDigit or not hasSpecialChar:
            raise ValidationError("La contraseña necesita al menos un número una mayúscula y un carácter especial")


        if field.data != form.passwordRepeat.data:
            raise ValidationError("No coinciden las contraseñas")






    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("No coinciden las contraseñas")


class LoginForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=20, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    recuerdame = BooleanField(label="Recuerdame")
