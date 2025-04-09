from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import main
    app.register_blueprint(main)

    return app
from flask import Flask
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = "segredo-super-seguro"

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)
