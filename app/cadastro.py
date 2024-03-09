from flask import Blueprint, render_template, request, redirect, url_for
import requests

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastro')
def cadastro_view():
    return render_template('cadastro.html')

@cadastro.route("/cadastro-in", methods=["POST"])
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
        return redirect(url_for('login.login_view'))  # assuming 'login_view' is the function name in 'login' blueprint
    except Exception as e:
        return redirect(url_for('cadastro.cadastro_view'))  # changed 'cadastro' to 'cadastro.cadastro_view'