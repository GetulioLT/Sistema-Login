# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

# Definindo o blueprint para a rota home
homeBlue = Blueprint('homeBlue', __name__)

# Definindo a rota para a página inicial
@homeBlue.route('/home')
@login_required  # Este decorador garante que o usuário deve estar logado para acessar esta rota
def home():
    return render_template('home.html')

# Definindo a rota para fazer logout
@homeBlue.route('/logout')
@login_required  # Este decorador garante que o usuário deve estar logado para acessar esta rota
def logout():
    logout_user()
    return redirect(url_for('loginBlue.login'))