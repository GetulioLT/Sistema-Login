# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
import requests
from app import User

# Definindo o blueprint para a rota de login
login = Blueprint('login', __name__)

# Definindo a rota para a página de login
@login.route('/')
def login_view():
    # Renderiza a página de login
    return render_template('login.html')

# Definindo a rota para o envio do formulário de login
@login.route("/login-in", methods=["POST"])
def login_in():
    # Obtendo o email do formulário
    email = request.form["email"]
    # Fazendo uma requisição GET para verificar o usuário
    login_response = requests.get(f"http://localhost:5001/user/{email}")

    try:
        # Se a requisição foi bem sucedida, faz o login do usuário
        email = login_response.json()["email"]

        user = User(email)
        login_user(user)

        # Redireciona para a página home
        return redirect(url_for('home.home_view'))  # assumindo que 'home_view' é o nome da função no blueprint 'home'
    except Exception as e:
        # Se ocorreu algum erro, redireciona de volta para a página de login
        return redirect(url_for('login.login_view'))  # mudou 'login' para 'login.login_view'