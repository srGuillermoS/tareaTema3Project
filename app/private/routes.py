import base64

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from werkzeug.datastructures import CombinedMultiDict

import app
from . import private
from .forms import FilterForm, CreateForm
from .models import Cliente


@private.route("/indexcliente/", methods=["GET", "POST"])
@login_required
def indexcliente():
    error = ""
    try:
        form = FilterForm(request.form)
        if form.validate_on_submit():
            clientes = Cliente.query.filter_by(nombre=form.nombre.data)
            return render_template("indexcliente.html", form=form, clientes=clientes)
        clientes = Cliente.query.all()
    except Exception as e:
        app.logger.exception(e.__str__())
        error = "Se ha producido un error inesperado intentelo más tarde"

    return render_template("indexcliente.html", form=form, clientes=clientes, error=error)


@private.route("/createcliente/", methods=["GET", "POST"])
@login_required
def createcliente():
    error = ""
    form = CreateForm(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
        try:
            cliente = Cliente()
            cliente.dni = form.dni.data
            cliente.nombre = form.nombre.data
            cliente.apellidos = form.apellidos.data
            encoded_bytes = base64.b64encode(form.imagen.data.read())
            max_length = 1024 * 1024
            if len(encoded_bytes) > max_length:
                form.imagen.errors.append("Tamaño máximo 1MB")
                app.logger.info("Cliente creado de forma correcta - " + cliente.dni)
                return render_template("registeruser.html", form=form)
            cliente.imagen = str(encoded_bytes).replace("b'", "").replace("'", "")
            cliente.saveCliente()
            return redirect(url_for("private.indexcliente"))
        except Exception as e:
            app.logger.exception(e.__str__())
            error = "No se ha podido realizar el alta, intentelo más tarde"

    return render_template("registeruser.html", form=form, error=error)
