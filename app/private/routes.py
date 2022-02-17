from flask import render_template

from . import private
from .models import Cliente




@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    clientes = Cliente.query.all()
    return render_template("indexcliente.html", clientes = clientes)