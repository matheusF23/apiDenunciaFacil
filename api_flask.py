from flask import Flask, escape, request
from resource import createUser, read

app = Flask(__name__)

@app.route('/user')
def user():
    cpf = request.args.get("cpf","")
    username = request.args.get("username", "")
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    senha = request.args.get("senha", "")

    dados = {
                "cpf": cpf,
                "username": username,
                "name": name,
                "email": email,
                "senha": senha
            }
    createUser(dados)
    return "ok"

@app.route('/select')
def selectUser():
    saida = read() 
    return saida

if __name__ == "__main__":
    app.run()