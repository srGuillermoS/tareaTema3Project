from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .log.logs import configure_loggin
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = '6LflODIfAAAAANh73jq3Omni-d6_CvkBDAxWgDvf'
app.config['RECAPTCHA_SECRET_KEY'] = '6LflODIfAAAAAEgwO9QvWEZMaM0QWeckdCxmErK-'
recaptcha = ReCaptcha(app)

app.secret_key = "ClaveSecreta"
#Cadena de conexión
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
#Desactivar la gestión de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instanciar la base de datos
db = SQLAlchemy(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)
login_manager.login_view = "login.loginuser"
logger = configure_loggin(__name__)

from .public import public
from .private import private
from .login import login
from .admin import admin


def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    app.register_blueprint(admin)
    return app