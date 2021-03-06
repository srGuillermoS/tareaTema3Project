from functools import wraps

from flask_login import current_user
from werkzeug.exceptions import abort

import app

#TODO Base de datos log
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        if not is_admin:
            abort(401)
            app.logger.warning("Acceso al area administración no identificado: " + getattr(current_user, 'username'))
        return f(*args, **kws)
    return decorated_function