from src.auth.models import * 
from src.requests.models import *

from src.extensions.db import db


def migrate(app):
    with app.app_context():
        db.drop_all()
        db.create_all()