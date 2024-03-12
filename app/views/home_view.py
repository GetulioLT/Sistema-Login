from app import app
from flask import render_template
from flask_login import login_required  # Importando a função login_required do flask_login


# Definindo a rota para a página inicial
@app.route('/home')
@login_required
def home():
    return render_template('home.html')