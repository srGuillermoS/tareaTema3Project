from flask import render_template, request

from . import private
from .forms import FilterForm, CreateForm
from .models import Cliente


@private.route("/indexcliente/", methods=["GET", "POST"])
def indexcliente():
    form = FilterForm(request.form)
    if form.validate_on_submit():
        clientes = Cliente.query.filter_by(nombre=form.nombre.data)
        return render_template("indexcliente.html",form=form, clientes=clientes)

    clientes = Cliente.query.all()
    return render_template("indexcliente.html", form=form, clientes=clientes)

@private.route("/createcliente/", methods=["GET", "POST"])
def createcliente():
    form = CreateForm(request.form)
#    if form.validate_on_submit():



    return render_template("createcliente.html", form=form)
