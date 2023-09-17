from flask_login import LoginManager
from src.apps.auth.models import User

login_manager = LoginManager()
login_manager.login_view = "auth.Login"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)