# Importando as bibliotecas necessárias
from flask import Flask
from flask_login import LoginManager, UserMixin

# Inicializando a aplicação Flask
app = Flask(__name__)
# Definindo a chave secreta para a sessão a partir de uma variável de ambiente
app.secret_key = "JaSoN"

# Inicializando o gerenciador de login
login_manager = LoginManager()
# Associando o gerenciador de login à aplicação Flask
login_manager.init_app(app)

# Definindo uma classe de usuário que herda de UserMixin
# UserMixin é uma classe que inclui implementações padrão para métodos como is_authenticated, is_active, etc.
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Definindo a função que carrega um usuário com base no ID
# Esta função é usada pelo Flask-Login para gerenciar as sessões de usuário
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Importando os blueprints para as rotas de login, cadastro e home
from .login import loginBlue as login_blueprint
from .cadastro import cadastroBlue as cadastro_blueprint
from .home import homeBlue as home_blueprint

# Registrando os blueprints na aplicação Flask
# Isso conecta as rotas definidas nos blueprints à aplicação
app.register_blueprint(login_blueprint)
app.register_blueprint(cadastro_blueprint)
app.register_blueprint(home_blueprint)