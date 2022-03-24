import base64

from flask import render_template, request, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict
import app
from . import login
from .forms import RegisterForm, LoginForm
from .models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


@login.route("/registeruser/", methods=["GET", "POST"])
def registeruser():
    error = ""
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        try:
            usuario = Usuario()
            usuario.username = form.username.data
            usuario.set_password(form.password.data)
            usuario.nombre = form.nombre.data
            usuario.apellidos = form.apellidos.data
            usuario.dni = form.dni.data
            usuario.create()
            return redirect(url_for('login.registeruser'))
        except Exception as e:
            app.logger.exception(e.__str__())
            error = "No se ha poddido realizar el registro" + e.__str__()

    return render_template("registeruser.html", form=form, error=error)


@login.route("/loginuser/", methods=["GET", "POST"])
def loginuser():
    error = ""
    try:
        if current_user.is_authenticated:
            return redirect(url_for('public.index'))
        form = LoginForm(request.form)
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            usuario = Usuario.get_by_username(username)
            if usuario and usuario.check_password(password):
                login_user(usuario)
                login_user(usuario, form.recuerdame.data)
                return redirect(url_for("private.indexcliente"))
            else:
                error = "Usuario y/o contraseña incorrecta"
    except Exception as e:
        app.logger.warning(e.__str__())
        error = "Nombre de usuario y/o contraseña incorrectos"
    return render_template("loginuser.html", form=form, error=error)


@app.login_manager.user_loader
def load_user(user_id):
    try:
        return Usuario.get_by_id(user_id)
    except:
        raise Exception("Ha ocurrido un error al realizar login")

@login.route("/logoutsession/")
@login_required
def logoutsession():
    try:
        logout_user()
        return redirect(url_for('public.index'))
    except:
        raise Exception("Ha ocurrido un error")
