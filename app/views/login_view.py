from app import app
from flask import render_template


# Definindo a rota para a página de login
@app.route('/login')
def login():
    return render_template('login.html')