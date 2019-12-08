
import sqlite3

## Classe Usuário ##
class Usuario():
    def createUser(self, kwargs):
        try:
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
            return "Usuário criado com sucesso!", 201
        except:
            return "Erro na criação de usuário", 400
        finally:
            cursor.close()
            conn.close()


    def readUser (self):
        try:
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
        except:
            return "Erro Insperado"
        finally:
            cursor.close()
            conn.close()

    def updateUser(self, _cpf, kwargs):
        try:
            cpf = kwargs["cpf"]
            username = kwargs["username"]
            name = kwargs["name"]
            email = kwargs["email"]
            senha = kwargs["senha"]

            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()

            cursor.execute("""UPDATE usuario SET cpf = ?, username = ?, nome = ?, email = ?, senha = ? 
                            WHERE cpf = ?""", (cpf, username, name, email, senha, _cpf))

            conn.commit()
            return "Usuário atualizado com sucesso!", 201
        except:
            return "Erro na atualização de usuário", 400
        finally:
            cursor.close()
            conn.close()


## Classe Motorista ##