import base64

from flask import render_template, request, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict

from . import login
from .forms import RegisterForm
from .models import Usuario


@login.route("/registeruser/", methods=["GET", "POST"])
def registeruser():
    error = ""
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
            error = "No se ha podido dar de alta " + e.__str__()



    return render_template("registeruser.html", form=form, error = error)



