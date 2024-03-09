from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
import requests
from app import User

login = Blueprint('login', __name__)

@login.route('/')
def login_view():
    return render_template('login.html')

@login.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]
    # Faz uma requisição para verificar o usuário
    login_response = requests.get(f"http://localhost:5001/user/{email}")

    try:
        email = login_response.json()["email"]

        user = User(email)
        login_user(user)

        return redirect(url_for('home.home_view'))  # assuming 'home_view' is the function name in 'home' blueprint
    except Exception as e:
        return redirect(url_for('login.login_view'))  # changed 'login' to 'login.login_view'