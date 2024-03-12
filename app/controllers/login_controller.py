# app/controllers/login_controller.py
from flask import Blueprint, request, redirect, url_for
from flask_login import login_user  # Importando a função login_user do flask_login
from app.models.user_model import User  # Importando a classe User
import requests

loginBlue = Blueprint("loginBlue", __name__)  # Criando uma instância da classe Blueprint

@loginBlue.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    # Fazendo uma requisição GET para verificar se o usuário existe
    login_response = requests.get(f"http://localhost:5001/user/{email}")

    try:
        email = login_response.json()["email"]

        user = User(email)  # Criando uma instância da classe User
        login_user(user)  # Fazendo login do usuário

        return redirect(url_for('homeBlue.home'))  # Redirecionando para a página inicial se o login for bem-sucedido
    except Exception as e:
        return redirect(url_for('loginBlue.login'))  # Redirecionando para a página de login se o login falhar