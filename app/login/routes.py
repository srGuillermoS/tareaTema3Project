import base64

from flask import render_template, request, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict

from . import login
from .forms import FilterForm, CreateForm
from .models import Usuario


@login.route("/indexcliente/", methods=["GET", "POST"])
def indexcliente():
    form = FilterForm(request.form)
    if form.validate_on_submit():
        clientes = Cliente.query.filter_by(nombre=form.nombre.data)
        return render_template("indexcliente.html", form=form, clientes=clientes)

    clientes = Cliente.query.all()
    return render_template("indexcliente.html", form=form, clientes=clientes)


@login.route("/createcliente/", methods=["GET", "POST"])
def createcliente():
    form = CreateForm(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
        cliente = Cliente()
        cliente.dni = form.dni.data
        cliente.nombre = form.nombre.data
        cliente.apellidos = form.apellidos.data
        encoded_bytes = base64.b64encode(form.imagen.data.read())
        max_length = 1024*1024
        if len(encoded_bytes) > max_length:
            form.imagen.errors.append("Tamaño máximo 1MB")
            return render_template("createcliente.html", form=form)

        cliente.imagen = str(encoded_bytes).replace("b'", "").replace("'", "")
        cliente.saveCliente()
        return redirect(url_for("private.indexcliente"))

    return render_template("createcliente.html", form=form)
