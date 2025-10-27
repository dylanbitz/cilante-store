from flask import Blueprint

assistant = Blueprint('assistant', __name__)

from . import routes