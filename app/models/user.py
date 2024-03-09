# app/models/user.py
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

def load_user(user_id):
    return User(user_id)