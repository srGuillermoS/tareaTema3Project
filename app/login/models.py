from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"


    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise Exception("Error al hacer el registro en la base datos")


    @staticmethod
    def get_by_id(id):
        try:
            return Usuario.query.get(id)
        except:
            raise Exception("Ha ocurrido un error")


    @staticmethod
    def get_by_username(username):
        try:
            return Usuario.query.filter_by(username=username).first()
        except:
            raise Exception("Ha ocurrido un error")


    def set_password(self, password):
        method = "pbkdf2:sha256:260000"
        self.password = generate_password_hash(password, method=method)  # Por defecto sha256

    def check_password(self, password):
        return check_password_hash(self.password, password)