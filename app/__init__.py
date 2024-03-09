from flask import Flask
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.secret_key = "jason"

login_manager = LoginManager()
login_manager.init_app(app)

# Define uma classe de usuário que herda de UserMixin
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Função para carregar um usuário com base no ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

from .login import login as login_blueprint
from .cadastro import cadastro as cadastro_blueprint
from .home import home as home_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(cadastro_blueprint)
app.register_blueprint(home_blueprint)