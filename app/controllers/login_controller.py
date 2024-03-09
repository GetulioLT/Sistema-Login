# app/controllers/login_controller.py
from flask import render_template, request, redirect, url_for
from flask_login import login_user  # Importando a função login_user do flask_login
from app import app
from app.models.user import User  # Importando a classe User
import requests

@app.route('/login')
def login():
    return render_template('login.html')  # Renderizando a página de login

@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    # Fazendo uma requisição GET para verificar se o usuário existe
    login_response = requests.get(f"http://localhost:5001/user/{email}")

    try:
        email = login_response.json()["email"]

        user = User(email)  # Criando uma instância da classe User
        login_user(user)  # Fazendo login do usuário

        return redirect(url_for('home'))  # Redirecionando para a página inicial se o login for bem-sucedido
    except Exception as e:
        return redirect(url_for('login'))  # Redirecionando para a página de login se o login falhar