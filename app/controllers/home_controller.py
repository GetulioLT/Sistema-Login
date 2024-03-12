# app/controllers/home_controller.py
from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user  # Importando as funções necessárias do flask_login

homeBlue = Blueprint('homeBlue', __name__)  # Criando uma instância da classe Blueprint

# Definindo a rota para fazer logout
@homeBlue.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('loginBlue.login'))