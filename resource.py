
import sqlite3

conn = sqlite3.connect('denuncia.db')

def read (id):

    return {"id":id, "local": "shopping da ilha"} 