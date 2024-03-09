# app/controllers/home_controller.py
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user
from app import app

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))