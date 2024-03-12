# app/views/home_view.py
from app.controllers.home_controller import homeBlue  # Importando a instância da classe Blueprint do controlador home_controller   
from flask import render_template
from flask_login import login_required  # Importando a função login_required do flask_login


# Definindo a rota para a página inicial
@homeBlue.route('/home')
@login_required
def home():
    return render_template('home.html')