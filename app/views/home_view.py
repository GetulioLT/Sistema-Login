from app.controllers.home_controller import homeBlue  # Importando a instância da classe Blueprint do controlador home_controller   
from flask import render_template
from flask_login import login_required  # Importando a função login_required do flask_login


@homeBlue.route('/home')
@login_required  # A rota '/home' requer que o usuário esteja logado
def home():
    return render_template('home.html')  # Renderizando a página inicial