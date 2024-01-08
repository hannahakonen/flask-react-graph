#main blueprint creation

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


from .config import MainConfig

frequencies = MainConfig.FREQUENCIES
intensities = MainConfig.INTENSITIES

from . import views, errors