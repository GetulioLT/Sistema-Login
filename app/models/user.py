# app/models/user.py
from flask_login import UserMixin  # Importando a classe UserMixin do flask_login

class User(UserMixin):  # Definindo a classe User que herda de UserMixin
    def __init__(self, id):  # Método construtor da classe User
        self.id = id  # Atribuindo o id passado como argumento ao atributo id da instância

def load_user(user_id):  # Função para carregar um usuário
    return User(user_id)  # Retornando uma instância da classe User com o id passado como argumento