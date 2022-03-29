from flask import render_template, abort
from flask_login import login_required, current_user

from . import admin
from ..auth.decorator import admin_required
from ..login.models import Usuario
import app

@admin.route('/adminindex/', methods=["GET", "POST"])
@login_required
@admin_required
def adminindex():
    try:
        usuarios = Usuario.query.all()
        app.logger.info("Listado de usuario se ha cargado de forma correcta" )
    except Exception as e:
        app.logger.exception(e.__str__())
    return render_template("adminindex.html", usuarios=usuarios)



