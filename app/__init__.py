# app/__init__.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager  # Importando a classe LoginManager do flask_login
from .models.user_model import load_user  # Importando a classe User e a função load_user

app = Flask(__name__)  # Criando uma instância da classe Flask
app.secret_key = "jason"  # Definindo a chave secreta da aplicação

login_manager = LoginManager()  # Criando uma instância da classe LoginManager
login_manager.init_app(app)  # Inicializando o gerenciador de login com a aplicação
login_manager.user_loader(load_user)  # Definindo a função que carrega um usuário

from app.controllers import cadastro_controller, home_controller, login_controller  # Importando os controladores
from app.views import cadastro_view, login_view, home_view  # Importando as views


from .controllers.cadastro_controller import cadastroBlue  # Importando a instância da classe Blueprint do controlador cadastro_controller  
from .controllers.home_controller import homeBlue  # Importando a instância da classe Blueprint do controlador home_controller  
from .controllers.login_controller import loginBlue  # Importando a instância da classe Blueprint do controlador login_controller4


app.register_blueprint(cadastroBlue)  # Registrando a instância da classe Blueprint do controlador cadastro_controller  
app.register_blueprint(homeBlue)  # Registrando a instância da classe Blueprint do controlador home_controller
app.register_blueprint(loginBlue)  # Registrando a instância da classe Blueprint do controlador login_controller

@app.route('/')  # Definindo a rota raiz da aplicação
def index():
    return redirect(url_for('loginBlue.login'))  # Redirecionando para a página de login