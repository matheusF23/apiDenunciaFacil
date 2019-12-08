
import sqlite3

## Classe Usuário ##
class Usuario():
    def createUser(self, kwargs):
        cpf = kwargs["cpf"]
        username = kwargs["username"]
        name = kwargs["name"]
        email = kwargs["email"]
        senha = kwargs["senha"]

        conn = sqlite3.connect('denunciafacil.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO usuario(cpf, username, nome, email, senha)
                        VALUES(?,?,?,?,?)""", (cpf, username, name, email, senha))

        conn.commit()
        conn.close()


    def readUser (self):
        conn = sqlite3.connect('denunciafacil.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                        SELECT * FROM usuario;
                        """)
        
        out = []
        dictionaryList = []
        for linha in cursor.fetchall():
            out.append(linha)

        for i in out:
            montaDict = {
                        "cpf": i[0],
                        "username": i[2],
                        "name": i[3],
                        "email": i[1],
                        "senha": i[4]
                    }
            dictionaryList.append(montaDict)

        return dictionaryList

    def updateUser(self, cpf, kwargs):
        username = ""
        name = ""
        email = ""
        senha = ""

        conn = sqlite3.connect('denunciafacil.db')
        cursor = conn.cursor()
        
        for key, value in kwargs.items():
            if(key == "cpf"):
                cpf = value
            elif(key == "username"):
                username = value
            elif(key == "name"):
                name = value
            elif(key == "email"):
                email = value
            elif(key == "senha"):
                senha = value

        cursor.execute("""UPDATE usuario SET username = ?, name = ?, email = ?, senha = ? 
                        WHERE id = ?""", (username, name, email, senha))

        conn.commit()
        conn.close()


## Classe Motorista ##