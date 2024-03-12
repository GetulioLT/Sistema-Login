# app/controllers/home_controller.py
from flask import redirect, url_for
from flask_login import login_required, logout_user  # Importando as funções necessárias do flask_login
from app import app


# Definindo a rota para fazer logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))