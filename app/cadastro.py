# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, request, redirect, url_for
import requests

# Definindo o blueprint para a rota de cadastro
cadastroBlue = Blueprint('cadastroBlue', __name__)

# Definindo a rota para a página de cadastro
@cadastroBlue.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Definindo a rota para o envio do formulário de cadastro
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