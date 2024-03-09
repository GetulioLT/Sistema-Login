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

    # Faz uma requisição para cadastrar o usuário
    cadastro_response = requests.post("http://localhost:5001/user", json=data)
    try:
        cadastro_response.json()["email"]
        return redirect(url_for('login'))
    except Exception as e:
        return redirect(url_for('cadastro'))