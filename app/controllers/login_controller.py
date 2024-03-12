# app/controllers/login_controller.py
from flask import request, redirect, url_for
from flask_login import login_user  # Importando a função login_user do flask_login
from app import app
from app.models.user import User  # Importando a classe User
import requests


# Definindo a rota para fazer login
@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    # Fazendo uma requisição GET para obter informações do usuário
    response = requests.get(f"http://localhost:5001/user/{email}")
    if response.status_code == 200:
        user = User(email)
        login_user(user)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))