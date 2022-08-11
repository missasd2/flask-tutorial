"""
View subclass
"""

from flask import (
    Blueprint, jsonify
)


from flaskr.db import get_db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<int:id>', methods=["GET"])
def get_user_by_id(id):
    res = {
        "code": 200,
        "message": {
            "mes1": "Hello %s"%id
        }
    }
    return res


