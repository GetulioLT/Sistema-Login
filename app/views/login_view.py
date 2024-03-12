from app.controllers.login_controller import loginBlue  # Importando a instância da classe Blueprint do controlador login_controller
from flask import render_template


@loginBlue.route('/login')
def login():
    return render_template('login.html')  # Renderizando a página de login