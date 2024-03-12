# api/views/login_view.py
from app.controllers.login_controller import loginBlue  # Importando a instância da classe Blueprint do controlador login_controller
from flask import render_template


# Definindo a rota para a página de login
@loginBlue.route('/login')
def login():
    return render_template('login.html')