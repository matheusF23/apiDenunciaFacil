from flask import Flask, escape, request, jsonify
from resource import UserRepository, OccurrenceRepository
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


## Occurrence routes ##
# Create Occurrence
@app.route('/occurrence/<string:cpf>/', methods=['POST'])
def createOccurrence(cpf):
    validateOccurrenceCreate = Rules(cpf).userValidate()
    if (validateOccurrenceCreate == 1):
        occurrence = OccurrenceRepository()
        data = request.get_json()
        return occurrence.createOccurrence(data)
    else:
        return "ERROR! User not found..", 404

# View Occurrence
@app.route('/occurrence', methods=['GET'])
def selectOccurrence():
    occurrence = OccurrenceRepository()
    out = occurrence.readOccurrence(None)
    return jsonify(out), 200

# View Occurrence by Id
@app.route('/occurrence/<string:id>', methods=['GET'])
def selectOccurrenceById(id):
    occurrence = OccurrenceRepository()
    out = occurrence.readOccurrence(id) 
    return jsonify(out), 200

# View Occurrence by User
@app.route('/occurrence/user/<string:cpf>', methods=['GET'])
def selectOccurrenceByUser(cpf):
    occurrence = OccurrenceRepository()
    out = occurrence.readOccurrenceByUser(cpf)
    return jsonify(out), 200

# Update Occurrence
@app.route('/occurrence/<string:id>/', methods=['PUT'])
def updatOccurrence(id):
    validateOccurrenceUpdate = Rules(None).occurrenceValidate(id)
    if (validateOccurrenceUpdate == 1):
        occurrence = OccurrenceRepository()
        data = request.get_json()
        return occurrence.updateOccurrence(id, data)
    else:
        return "ERROR! Occurrence not found.", 404
    

# Delete Occurrence
@app.route('/occurrence/<string:id>', methods=['DELETE'])
def deleteOccurrence(id):
    validateOccurrenceDelete = Rules(None).occurrenceValidate(id)
    if (validateOccurrenceDelete == 1):
        occurrence = OccurrenceRepository()
        return occurrence.deleteOccurrence(id)
    else:
        return "ERROR! Occurrence not found.", 404
    

if __name__ == "__main__":
    app.run(debug=True)
