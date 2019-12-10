from resource import UserRepository, OcurrenceRepository

class Rules():
    def __init__ (self, cpf):
        self.cpf = cpf
        self.user = UserRepository()
        self.ocurrence = OcurrenceRepository()

    def userValidate(self):
        if(self.user.readUser(self.cpf) == []):
            return 0
        else:
            return 1
    
    def ocurrenceValidate(self, id):
        if(self.ocurrence.readOcurrence(id) == []):
            return 0
        else:
            return 1
    
    # def validateDeleteUpdate(self):
    #     if(self.user.readUser(self.cpf) == []):
    #         return 0
    #     else:
    #         return 1

    def validateLoginUser(self, email, senha):
        UserLis = self.user.readUser(None)
        for i in UserLis:
            if(i["email"] == email):
                if(i["senha"] == senha):
                    return "Ok", 200
                else:
                    return "Invalid Key", 400
        return "User not found", 404
            
