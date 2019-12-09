
import sqlite3

## Classe Usuário ##
class UserRepository():
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
            return "User successfully created!", 201
        except:
            return "Error creating user", 400
        finally:
            cursor.close()
            conn.close()


    def readUser (self, _cpf):
        try:
            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()
            if(_cpf):
                print(_cpf)
                cursor.execute("""
                            SELECT * FROM usuario WHERE cpf = ?;
                            """, (_cpf,))
            else:
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
            return "Unexpected error"
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
            return "User updated successfully!", 201
        except:
            return "Error updating user!", 400
        finally:
            cursor.close()
            conn.close()
    
    def deleteUser(self, _cpf):
        try:
            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()

            cursor.execute("""DELETE FROM usuario WHERE cpf = ?""", (_cpf,))

            conn.commit()
            return "User deleted successfully!"
        except:
            return "Unexpected error!"
        finally:
            cursor.close()
            conn.close()

## Classe Ocorrência ##
class OcurrenceRepository():
    def createOcurrence(self, kwargs):
        try:
            titulo_ocorrencia = kwargs["titulo_ocorrencia"]
            tipo_ocorrencia = kwargs["tipo_ocorrencia"]
            descricao = kwargs["descricao"]
            data = kwargs["data"]
            hora = kwargs["hora"]
            bairro = kwargs["bairro"]
            rua = kwargs["rua"]
            cidade = kwargs["cidade"]
            estado = kwargs["estado"]
            cpf_usuario = kwargs["cpf_usuario"]
            placa = kwargs["placa"]

            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO ocorrencia(titulo, tipo_ocorrencia, descricao, data, hora,
                            bairro, rua, cidade, estado, cpf_usuario, placa)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (titulo_ocorrencia, tipo_ocorrencia, descricao, data, 
                            hora, bairro, rua, cidade, estado, cpf_usuario, placa))
            conn.commit()
            return "Occurrence successfully registered!", 201
        except:
            return "Error in occurrence registration!", 400
        finally:
            cursor.close()
            conn.close()


    def readOcurrence (self, _id):
        try:
            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()
            
            if(_id):
                cursor.execute("""
                            SELECT * FROM ocorrencia WHERE id = ?;
                            """, (_id,))
            else:
                cursor.execute("""
                                SELECT * FROM ocorrencia;
                                """)
            
            out = []
            dictionaryList = []
            for linha in cursor.fetchall():
                out.append(linha)

            for i in out:
                montaDict = {
                            "id": i[0],
                            "cpf_usuario": i[10],
                            "placa": i[11],
                            "titulo_ocorrencia": i[1],
                            "tipo_ocorrencia": i[2],
                            "descricao": i[3],
                            "data": i[4],
                            "hora": i[5],
                            "bairro": i[6],
                            "rua": i[7],
                            "cidade": i[8],
                            "estado": i[9]
                        }
                dictionaryList.append(montaDict)

            return dictionaryList
        except:
            return "Unexpected error"
        finally:
            cursor.close()
            conn.close()

    def updateOcurrence(self, _id, kwargs):
        try:
            titulo_ocorrencia = kwargs["titulo_ocorrencia"]
            tipo_ocorrencia = kwargs["tipo_ocorrencia"]
            descricao = kwargs["descricao"]
            data = kwargs["data"]
            hora = kwargs["hora"]
            bairro = kwargs["bairro"]
            rua = kwargs["rua"]
            cidade = kwargs["cidade"]
            estado = kwargs["estado"]
            cpf_usuario = kwargs["cpf_usuario"]
            placa = kwargs["placa"]

            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()

            cursor.execute("""UPDATE ocorrencia SET titulo = ?, tipo_ocorrencia = ?, descricao = ?, 
                            data = ?, hora = ?, bairro = ?, rua = ?, cidade = ?, estado = ?, cpf_usuario = ?,
                            placa = ? WHERE id = ?""", (titulo_ocorrencia, tipo_ocorrencia, descricao, data, 
                            hora, bairro, rua, cidade, estado, cpf_usuario, placa, _id))

            conn.commit()
            return "Occurrence successfully updated!", 201
        except:
            return "Unexpected error", 400
        finally:
            cursor.close()
            conn.close()
    
    def deleteOcurrence(self, _id):
        try:
            conn = sqlite3.connect('denunciafacil.db')
            cursor = conn.cursor()

            cursor.execute("""DELETE FROM ocorrencia WHERE id = ?""", (_id,))

            conn.commit()
            return "Occurrence deleted successfully!"
        except:
            return "Unexpected error"
        finally:
            cursor.close()
            conn.close()