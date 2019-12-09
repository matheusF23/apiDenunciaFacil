from resource import UserRepository

class Rules():
    def __init__ (self, cpf):
        self.cpf = cpf
        self.user = UserRepository()

    def validateUserCreate(self):
        if(self.user.readUser(self.cpf) == []):
            return 1
        else:
            return 0
    
    def validateUserUpdate(self):
        if(self.user.readUser(self.cpf) == []):
            return 0
        else:
            return 1
