from flask import Flask, escape, request, jsonify
from resource import UserRepository, OcurrenceRepository
from businessrules.rules import Rules

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to API Denúncia Fácil"

## User routes ##
# Create User
@app.route('/user/<string:cpf>/', methods=['POST'])
def createUser(cpf):
    validateUserCreate = Rules(cpf).validateUserCreate()
    if (validateUserCreate == 1):
        user = UserRepository()
        data = request.get_json()
        return user.createUser(data)
    else:
        return "ERROR! User already exists.", 400

# View User
@app.route('/user/', methods=['GET'])
def selectUser():
    user = UserRepository()
    out = user.readUser(None)
    return jsonify(out), 200

# View User by CPF
@app.route('/user/<string:cpf>/', methods=['GET'])
def selectUserByCPF(cpf):
    user = UserRepository()
    out = user.readUser(cpf) 
    return jsonify(out), 200

# View User by email
@app.route('/user/<string:email>/<string:senha>/', methods=['GET'])
def selectUserByEmail(email, senha):
    
    return Rules(None).validateLoginUser(email, senha)

# Update User
@app.route('/user/<string:cpf>/', methods=['PUT'])
def updateUser(cpf):
    validateUserUpdate = Rules(cpf).validateUserUpdate()
    if (validateUserUpdate == 1):
        user = UserRepository()
        data = request.get_json()
        return user.updateUser(cpf, data)
    else:
        return "ERROR! User not found.", 404

# Delete User
@app.route('/user/<string:cpf>/', methods=['DELETE'])
def deleteUser(cpf):
    user = UserRepository()
    return user.deleteUser(cpf)


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
