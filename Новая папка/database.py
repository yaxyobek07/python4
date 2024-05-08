import sqlite3

def createtable():
    database =sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS foods(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name VARCHAR,
    price INTEGER,
    about VARCHAR,
    category VARCHAR
    )''')
    database.commit()
    database.close()

createtable()




def addcolumntable():
    database =sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''ALTER TABLE foods ADD image BLOB''')
    database.commit()
    database.close()

addcolumntable()

