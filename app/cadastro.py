# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, request, redirect, url_for
import requests

# Definindo o blueprint para a rota de cadastro
cadastro = Blueprint('cadastro', __name__)

# Definindo a rota para a página de cadastro
@cadastro.route('/cadastro')
def cadastro_view():
    # Renderiza a página de cadastro
    return render_template('cadastro.html')

# Definindo a rota para o envio do formulário de cadastro
@cadastro.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    # Obtendo os dados do formulário
    email = request.form["email"]
    password = request.form["password"]

    # Preparando os dados para a requisição
    data = {
        "email": email,
        "password": password
    }

    # Fazendo uma requisição POST para cadastrar o usuário
    cadastro_response = requests.post("http://localhost:5001/user", json=data)
    try:
        # Se a requisição foi bem sucedida, redireciona para a página de login
        cadastro_response.json()["email"]
        return redirect(url_for('login.login_view'))  # assuming 'login_view' is the function name in 'login' blueprint
    except Exception as e:
        # Se ocorreu algum erro, redireciona de volta para a página de cadastro
        return redirect(url_for('cadastro.cadastro_view'))  # changed 'cadastro' to 'cadastro.cadastro_view'