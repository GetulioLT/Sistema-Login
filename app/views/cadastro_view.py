from app.controllers.cadastro_controller import cadastroBlue
from flask import render_template


@cadastroBlue.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')