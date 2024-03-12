# app/controllers/home_controller.py
from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user  # Importando as funções necessárias do flask_login

homeBlue = Blueprint('homeBlue', __name__)  # Criando uma instância da classe Blueprint

@homeBlue.route('/logout')
@login_required  # A rota '/logout' requer que o usuário esteja logado
def logout():
    logout_user()  # Fazendo logout do usuário
    return redirect(url_for('loginBlue.login'))  # Redirecionando o usuário para a página de login após o logout