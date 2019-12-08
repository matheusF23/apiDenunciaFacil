from flask import Flask, escape, request, jsonify
from resource import Usuario

app = Flask(__name__)

## Rotas para Usuário ##
@app.route('/')
def home():
    return "Seja Bem Vindo à API Denúncia Fácil"

@app.route('/user')
def user():
    usuario = Usuario()
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
    usuario.createUser(dados)
    return "Usuário criado com sucesso", 201

@app.route('/user/select')
def selectUser():
    usuario = Usuario()
    saida = usuario.readUser() 
    return jsonify(saida), 200

@app.route('/user/update/<string:_cpf>/')
def updateUser(_cpf):
    usuario = Usuario()

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

    usuario.updateUser(_cpf, dados)
    return "Usuário atualizado com sucesso", 200

if __name__ == "__main__":
    app.run(debug=True)