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

    def validateLoginUser(self, email, senha):
        UserLis = self.user.readUser(None)
        for i in UserLis:
            if(i["email"] == email):
                if(i["senha"] == senha):
                    return "Ok", 200
                else:
                    return "Invalid Key", 400
        return "User not found", 404
            
