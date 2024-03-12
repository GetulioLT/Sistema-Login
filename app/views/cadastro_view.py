from app import app
from flask import render_template


# Definindo a rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')