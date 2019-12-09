from flask import Flask, escape, request, jsonify
from resource import UserRepository, OcurrenceRepository

app = Flask(__name__)

@app.route('/')
def home():
    return "Seja Bem Vindo à API Denúncia Fácil"

## User routes ##
# Create User
@app.route('/user/<string:_cpf>/', methods=['POST'])
def createUser(_cpf):
    user = UserRepository()
    data = request.get_json()
    return user.createUser(data)

# View User
@app.route('/user/', methods=['GET'])
def selectUser():
    user = UserRepository()
    out = user.readUser(None) 
    return jsonify(out), 200
# View User by CPF
@app.route('/user/<string:_cpf>/', methods=['GET'])
def selectUserByCPF(_cpf):
    user = UserRepository()
    out = user.readUser(_cpf) 
    return jsonify(out), 200

# Update User
@app.route('/user/<string:_cpf>/', methods=['PUT'])
def updateUser(_cpf):
    user = UserRepository()
    data = request.get_json()
    return user.updateUser(_cpf, data)

# Delete User
@app.route('/user/<string:_cpf>/', methods=['DELETE'])
def deleteUser(_cpf):
    user = UserRepository()
    return user.deleteUser(_cpf)


## Ocurrence routes ##
# Create Ocurrence
@app.route('/ocurrence/', methods=['POST'])
def ocorrencia():
    ocurrence = OcurrenceRepository()
    dados = request.get_json()
    return ocurrence.createOcurrence(dados)

# View Ocurrence
@app.route('/ocurrence/', methods=['GET'])
def selectOcurrence():
    ocurrence = OcurrenceRepository()
    out = ocurrence.readOcurrence(None)
    return jsonify(out), 200

# View Ocurrence by Id
@app.route('/ocurrence/<string:_id>/', methods=['GET'])
def selectOcurrenceById(_id):
    ocurrence = OcurrenceRepository()
    out = ocurrence.readOcurrence(_id) 
    return jsonify(out), 200

# Update Ocurrence
@app.route('/ocurrence/<string:_id>/', methods=['PUT'])
def updatOcurrence(_id):
    ocurrence = OcurrenceRepository()
    data = request.get_json()
    return ocurrence.updateOcurrence(_id, data)

# Delete Ocurrence
@app.route('/ocurrence/<string:_id>', methods=['DELETE'])
def deleteOcurrence(_id):
    ocurrence = OcurrenceRepository()
    return ocurrence.deleteOcurrence(_id)


if __name__ == "__main__":
    app.run(debug=True)