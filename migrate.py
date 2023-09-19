from src.apps.auth.models import * 
from src.apps.requests.models import *

from src.extensions.db import db


def migrate(app):
    with app.app_context():
        db.drop_all()
        db.create_all()