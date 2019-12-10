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
    validateUserCreate = Rules(cpf).userValidate()
    if (validateUserCreate == 0):
        user = UserRepository()
        data = request.get_json()
        return user.createUser(data)
    else:
        return "ERROR! User already exists.", 400

# View User
@app.route('/user', methods=['GET'])
def selectUser():
    user = UserRepository()
    out = user.readUser(None)
    return jsonify(out), 200

# View User by CPF
@app.route('/user/<string:cpf>', methods=['GET'])
def selectUserByCPF(cpf):
    user = UserRepository()
    out = user.readUser(cpf) 
    return jsonify(out), 200

# Login Validate
@app.route('/user/<string:email>/<string:senha>', methods=['GET'])
def selectUserByEmail(email, senha):
    return Rules(None).validateLoginUser(email, senha)

# Update User
@app.route('/user/<string:cpf>/', methods=['PUT'])
def updateUser(cpf):
    validateUserUpdate = Rules(cpf).userValidate()
    if (validateUserUpdate == 1):
        user = UserRepository()
        data = request.get_json()
        return user.updateUser(cpf, data)
    else:
        return "ERROR! User not found.", 404

# Delete User
@app.route('/user/<string:cpf>', methods=['DELETE'])
def deleteUser(cpf):
    validateUserDelete = Rules(cpf).userValidate()
    if (validateUserDelete == 1):
        user = UserRepository()
        return user.deleteUser(cpf)
    else:
        return "ERROR! User not found.", 404


## Ocurrence routes ##
# Create Ocurrence
@app.route('/ocurrence/<string:cpf>/', methods=['POST'])
def createOcurrence(cpf):
    validateOcurrenceCreate = Rules(cpf).userValidate()
    if (validateOcurrenceCreate == 1):
        ocurrence = OcurrenceRepository()
        data = request.get_json()
        return ocurrence.createOcurrence(data)
    else:
        return "ERROR! User not found..", 404

# View Ocurrence
@app.route('/ocurrence', methods=['GET'])
def selectOcurrence():
    ocurrence = OcurrenceRepository()
    out = ocurrence.readOcurrence(None)
    return jsonify(out), 200

# View Ocurrence by Id
@app.route('/ocurrence/<string:id>', methods=['GET'])
def selectOcurrenceById(id):
    ocurrence = OcurrenceRepository()
    out = ocurrence.readOcurrence(id) 
    return jsonify(out), 200

# View Ocurrence by User
@app.route('/ocurrence/user/<string:cpf>', methods=['GET'])
def selectOcurrenceByUser(cpf):
    ocurrence = OcurrenceRepository()
    out = ocurrence.readOcurrenceByUser(cpf)
    return jsonify(out), 200

# Update Ocurrence
@app.route('/ocurrence/<string:id>/', methods=['PUT'])
def updatOcurrence(id):
    validateOcurrenceUpdate = Rules(None).ocurrenceValidate(id)
    if (validateOcurrenceUpdate == 1):
        ocurrence = OcurrenceRepository()
        data = request.get_json()
        return ocurrence.updateOcurrence(id, data)
    else:
        return "ERROR! Ocurrence not found.", 404
    

# Delete Ocurrence
@app.route('/ocurrence/<string:id>', methods=['DELETE'])
def deleteOcurrence(id):
    validateOcurrenceDelete = Rules(None).ocurrenceValidate(id)
    if (validateOcurrenceDelete == 1):
        ocurrence = OcurrenceRepository()
        return ocurrence.deleteOcurrence(id)
    else:
        return "ERROR! Ocurrence not found.", 404
    

if __name__ == "__main__":
    app.run(debug=True)
