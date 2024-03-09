# app/__init__.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager  # Importando a classe LoginManager do flask_login
from .models.user import User, load_user  # Importando a classe User e a função load_user

app = Flask(__name__)  # Criando uma instância da classe Flask
app.secret_key = "jason"  # Definindo a chave secreta da aplicação

login_manager = LoginManager()  # Criando uma instância da classe LoginManager
login_manager.init_app(app)  # Inicializando o gerenciador de login com a aplicação
login_manager.user_loader(load_user)  # Definindo a função que carrega um usuário

from app.controllers import cadastro_controller, home_controller, login_controller  # Importando os controladores

@app.route('/')  # Definindo a rota raiz da aplicação
def index():
    return redirect(url_for('login'))  # Redirecionando para a página de login

if __name__ == '__main__':
    app.run(debug=True)  # Rodando a aplicação em modo de debug