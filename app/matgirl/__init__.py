from flask import Blueprint

matgirl = Blueprint('matgirl', __name__)

from . import views
