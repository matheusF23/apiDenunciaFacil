from resource import UserRepository

class Rules():
    def validateUser(self, cpf):
        user = UserRepository()
        if(user.readUser(cpf) == []):
            return 1
        else:
            return 0
