# app/controllers/cadastro_controller.py
from flask import Blueprint, request, redirect, url_for
import requests

cadastroBlue = Blueprint("cadastroBlue", __name__)

@cadastroBlue.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    email = request.form["email"]
    password = request.form["password"]

    data = {
        "email": email,
        "password": password
    }

    # Fazendo uma requisição POST para cadastrar o usuário
    cadastro_response = requests.post("http://localhost:5001/user", json=data)
    try:
        cadastro_response.json()["email"]
        # Redirecionando para a rota '/login' se o cadastro for bem-sucedido
        return redirect(url_for('loginBlue.login'))  
    except Exception as e:
        # Redirecionando para a rota '/cadastro' se o cadastro falhar
        return redirect(url_for('cadastroBlue.cadastro'))  