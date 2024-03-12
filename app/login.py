# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
import requests
from app import User

# Definindo o blueprint para a rota de login
loginBlue = Blueprint('loginBlue', __name__)

# Definindo a rota para a página de login
@loginBlue.route('/')
def login():
    return render_template('login.html')

# Definindo a rota para fazer login
@loginBlue.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    # Fazendo uma requisição GET para obter informações do usuário
    response = requests.get(f"http://localhost:5001/user/{email}")
    if response.status_code == 200:
        user = User(email)
        login_user(user)
        return redirect(url_for('homeBlue.home'))
    else:
        return redirect(url_for('loginBlue.login'))