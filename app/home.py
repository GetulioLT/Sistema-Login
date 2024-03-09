# Importando as bibliotecas necessárias
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

# Definindo o blueprint para a rota home
home = Blueprint('home', __name__)

# Definindo a rota para a página home
@home.route('/home')
@login_required  # Este decorador garante que o usuário deve estar logado para acessar esta rota
def home_view():
    # Renderiza a página home
    return render_template('home.html')

# Definindo a rota para logout
@home.route('/logout')
@login_required  # Este decorador garante que o usuário deve estar logado para acessar esta rota
def logout():
    # Faz o logout do usuário
    logout_user()
    # Redireciona para a página de login
    return redirect(url_for('login.login_view'))