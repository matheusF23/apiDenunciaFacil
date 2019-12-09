from flask import Flask, escape, request, jsonify
from resource import Usuario, Ocorrencia

app = Flask(__name__)

@app.route('/')
def home():
    return "Seja Bem Vindo à API Denúncia Fácil"

## Rotas para Usuário ##
# Criar Usuário
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

# Visualizar usuários
@app.route('/user/select')
def selectUser():
    usuario = Usuario()
    saida = usuario.readUser() 
    return jsonify(saida), 200

# Atualizar Usuário
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

# Deletar Usuário
@app.route('/user/delete/<string:_cpf>')
def deleteUser(_cpf):
    usuario = Usuario()
    return usuario.deleteUser(_cpf)


## Rotas para Ocorrência ##
# Criar Ocorrência
@app.route('/ocorrencia')
def ocorrencia():
    ocorrencia = Ocorrencia()
    
    cpf_usuario = request.args.get("cpf_usuario")
    placa = request.args.get("placa")
    titulo_ocorrencia = request.args.get("titulo_ocorrencia")
    tipo_ocorrencia = request.args.get("tipo_ocorrencia")
    descricao = request.args.get("descricao")
    data = request.args.get("data")
    hora = request.args.get("hora")
    bairro = request.args.get("bairro")
    rua = request.args.get("rua")
    cidade = request.args.get("cidade")
    estado = request.args.get("estado")


    dados = {
                "cpf_usuario": cpf_usuario,
                "placa": placa,
                "titulo_ocorrencia": titulo_ocorrencia,
                "tipo_ocorrencia": tipo_ocorrencia,
                "descricao": descricao,
                "data": data,
                "hora": hora,
                "bairro": bairro,
                "rua": rua,
                "cidade": cidade,
                "estado": estado
            }
    return ocorrencia.createOcorrencia(dados)

# Visualizar Ocorrências
@app.route('/ocorrencia/select')
def selectOcorrencia():
    ocorrencia = Ocorrencia()
    saida = ocorrencia.readOcorrencia()
    return jsonify(saida), 200

# Atualizar Ocorrência
@app.route('/ocorrencia/update/<string:_id>/')
def updateOcorrencia(_id):
    ocorrencia = Ocorrencia()

    cpf_usuario = request.args.get("cpf_usuario")
    placa = request.args.get("placa")
    titulo_ocorrencia = request.args.get("titulo_ocorrencia")
    tipo_ocorrencia = request.args.get("tipo_ocorrencia")
    descricao = request.args.get("descricao")
    data = request.args.get("data")
    hora = request.args.get("hora")
    bairro = request.args.get("bairro")
    rua = request.args.get("rua")
    cidade = request.args.get("cidade")
    estado = request.args.get("estado")


    dados = {
                "cpf_usuario": cpf_usuario,
                "placa": placa,
                "titulo_ocorrencia": titulo_ocorrencia,
                "tipo_ocorrencia": tipo_ocorrencia,
                "descricao": descricao,
                "data": data,
                "hora": hora,
                "bairro": bairro,
                "rua": rua,
                "cidade": cidade,
                "estado": estado
            }
    return ocorrencia.updateOcorrencia(_id, dados)

# Deletar Ocorrência
@app.route('/ocorrencia/delete/<string:_id>')
def deleteOcorrencia(_id):
    ocorrencia = Ocorrencia()
    return ocorrencia.deleteOcorrencia(_id)


if __name__ == "__main__":
    app.run(debug=True)