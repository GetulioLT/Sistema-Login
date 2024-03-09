# app/__init__.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from .models.user import User, load_user

app = Flask(__name__)
app.secret_key = "jason"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(load_user)

from app.controllers import login_controller, home_controller, cadastro_controller

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)