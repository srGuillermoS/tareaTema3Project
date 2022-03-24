from app import db


class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String, nullable=False)

    def saveCliente(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            raise Exception("Error al guardar cliente en la base datos")