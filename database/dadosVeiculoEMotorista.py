import sqlite3

conn = sqlite3.connect('denunciafacil.db')
cursor = conn.cursor()

# cursor.execute("""INSERT INTO motorista(cpf, nome)
#                 VALUES(?,?)""", ("00000000000", "Infrator"))
# cursor.execute("""INSERT INTO veiculo(placa, cpf_motorista)
#                 VALUES(?,?)""", ("ABC0000", "00000000000"))
# conn.commit()

cursor.execute("""
SELECT * FROM motorista;
""")

for linha in cursor.fetchall():
    print(linha)

cursor.execute("""
SELECT * FROM veiculo;
""")

for linha in cursor.fetchall():
    print(linha)
cursor.execute("""
SELECT * FROM motorista m left join veiculo v on m.cpf = v.cpf_motorista;
""")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()