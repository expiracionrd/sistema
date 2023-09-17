from flask import Flask
from decouple import config
from src.extensions.db import db
from src.extensions.login import login_manager

from src.apps.auth.router import bp as auth_bp
from src.apps.requests.router import bp as req_bp


app = Flask(__name__)

app.config["SECRET_KEY"] = config("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(req_bp)

