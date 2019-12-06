from flask import Flask, escape, request
from resource import read

from createTable import createTable

createTable()

app = Flask(__name__)

@app.route('/')
def home():
    id = request.args.get("id", "00")
    return read(id)

@app.route('/ocorrencia')
def ocorrencia():
    return "ocorrencia"

if __name__ == "__main__":
    app.run()