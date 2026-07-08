from src.model.User import User

class Login:
    def __init__(self):
        self.__user = "admin"
        self.__password = "123"
    
    def execute(self, user: User) -> bool:
        if user.name == self.__user and user.password == self.__password:
            return True
        else:
            return False
