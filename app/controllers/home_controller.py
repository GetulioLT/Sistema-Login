# app/controllers/home_controller.py
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user  # Importando as funções necessárias do flask_login
from app import app

@app.route('/home')
@login_required  # A rota '/home' requer que o usuário esteja logado
def home():
    return render_template('home.html')  # Renderizando a página inicial

@app.route('/logout')
@login_required  # A rota '/logout' requer que o usuário esteja logado
def logout():
    logout_user()  # Fazendo logout do usuário
    return redirect(url_for('login'))  # Redirecionando o usuário para a página de login após o logout