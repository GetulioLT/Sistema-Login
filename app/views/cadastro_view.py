# api/views/cadastro_view.py
from app.controllers.cadastro_controller import cadastroBlue
from flask import render_template


# Definindo a rota para a página de cadastro
@cadastroBlue.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')