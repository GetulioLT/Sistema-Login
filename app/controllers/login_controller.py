# app/controllers/login_controller.py
from flask import render_template, request, redirect, url_for
from flask_login import login_user
from app import app
from app.models.user import User
import requests

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]
    # Faz uma requisição para verificar o usuário
    login_response = requests.get(f"http://localhost:5001/user/{email}")

    try:
        email = login_response.json()["email"]

        user = User(email)
        login_user(user)

        return redirect(url_for('home'))
    except Exception as e:
        return redirect(url_for('login'))