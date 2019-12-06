import sqlite3

def createTable():
    try:

        connection = sqlite3.connect('denuncia.db')

        mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                                Id int(11) NOT NULL,
                                Name varchar(250) NOT NULL,
                                Price float NOT NULL,
                                Purchase_date Date NOT NULL,
                                PRIMARY KEY (Id)) """

        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("Laptop Table created successfully ")

    except:
        print("Failed to create table")
    finally:
        connection.close()
        print("connection is closed")
