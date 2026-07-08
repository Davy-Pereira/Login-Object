from src.model.Login import Login
from src.model.User import User

login = Login()

user = User("admin", "123")

if login.execute(user):
    print("Login efetuado")
else:
    print("Erro ao logar")