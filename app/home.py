from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

home = Blueprint('home', __name__)

@home.route('/home')
@login_required
def home_view():
    return render_template('home.html')

@home.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login_view'))