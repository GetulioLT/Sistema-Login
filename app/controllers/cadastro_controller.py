# app/controllers/cadastro_controller.py
from flask import Blueprint, request, redirect, url_for
import requests

cadastroBlue = Blueprint("cadastroBlue", __name__)

# Definindo a rota para fazer cadastro
@cadastroBlue.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    email = request.form["email"]
    password = request.form["password"]

    data = {
        "email": email,
        "password": password
    }

    # Fazendo uma requisição POST para cadastrar o usuário
    response = requests.post("http://localhost:5001/user", json=data)
    if response.status_code == 201:
        return redirect(url_for('loginBlue.login'))
    else:
        return redirect(url_for('cadastroBlue.cadastro'))