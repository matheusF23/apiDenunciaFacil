
import sqlite3

conn = sqlite3.connect('denunciafacil.db')

def read (id):

    return {"id":id, "local": "shopping da ilha"} 