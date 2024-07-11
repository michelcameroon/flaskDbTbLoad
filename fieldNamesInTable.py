import sqlite3

from os import path

def names(db, tb):

    #connection = sqlite3.connect('instance/solarCalc4.db')
    connection = sqlite3.connect(db)

    #cursor = connection.execute('select * from panel')
    cursor = connection.execute('select * from ' + tb)

    names = list(map(lambda x: x[0], cursor.description))
    
    #for name in names:
    #    print(name)

    return names


if __name__ == '__main__':
    app.run(debug=True)

