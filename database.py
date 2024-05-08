import sqlite3


# def createtable():
#     database = sqlite3.connect('shaharlar.sqlite')
#     cursor = database.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS cities(
#     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name VARCHAR UNIQUE,
#     chatid INTEGER
#     )''')
#     database.commit()
#     database.close()
#
# createtable()


def registrshahar(name, chatid):
    database = sqlite3.connect('shaharlar.sqlite')
    cursor = database.cursor()
    cursor.execute('''SELECT name FROM cities WHERE name = ?''', (name, ))
    shahar = cursor.fetchone()

    database.close()
    if not shahar:
        database = sqlite3.connect('shaharlar.sqlite')
        cursor = database.cursor()
        cursor.execute('''INSERT INTO cities(name, chatid) VALUES(?, ?)''', (name, chatid))
        database.commit()
        database.close()
