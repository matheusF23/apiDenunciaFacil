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
    
    cpf = request.args.get("cpf")
    username = request.args.get("username")
    name = request.args.get("name")
    email = request.args.get("email")
    senha = request.args.get("senha")

    dados = {
                "cpf": cpf,
                "username": username,
                "name": name,
                "email": email,
                "senha": senha
            }
    return usuario.createUser(dados)

@app.route('/user/select')
def selectUser():
    usuario = Usuario()
    saida = usuario.readUser() 
    return jsonify(saida), 200

@app.route('/user/update/<string:_cpf>/')
def updateUser(_cpf):
    usuario = Usuario()

    cpf = request.args.get("cpf")
    username = request.args.get("username")
    name = request.args.get("name")
    email = request.args.get("email")
    senha = request.args.get("senha")

    dados = {
                "cpf": cpf,
                "username": username,
                "name": name,
                "email": email,
                "senha": senha
            }
   
    return usuario.updateUser(_cpf, dados)

if __name__ == "__main__":
    app.run(debug=True)