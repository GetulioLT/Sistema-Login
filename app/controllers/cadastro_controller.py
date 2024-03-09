# app/controllers/cadastro_controller.py
from flask import render_template, request, redirect, url_for
from app import app
import requests

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro-in", methods=["POST"])
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
        return redirect(url_for('login'))  
    except Exception as e:
        # Redirecionando para a rota '/cadastro' se o cadastro falhar
        return redirect(url_for('cadastro'))  