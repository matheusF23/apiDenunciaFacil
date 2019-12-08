
import sqlite3

def createUser(kwargs):
    cpf = ""
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

    cursor.execute("""INSERT INTO usuario(cpf, username, nome, email, senha)
                    VALUES(?,?,?,?,?)""", (cpf, username, name, email, senha))

    conn.commit()
    conn.close()


def read ():
    conn = sqlite3.connect('denunciafacil.db')
    cursor = conn.cursor()
    
    cursor.execute("""
                    SELECT * FROM usuario;
                    """)
    
    saida = cursor.fetchone()

    result = {
                "cpf": saida[0],
                "username": saida[2],
                "name": saida[3],
                "email": saida[1],
                "senha": saida[4]
            }

    return result