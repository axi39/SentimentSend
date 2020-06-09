### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020


import sqlite3
from sqlite3 import Error



def connect_db():
    '''
    Creates DB file SQLite3

    parameter(s): NA

    returns: connection (database connection object)
    '''
    
    connection = None
    try:
        connection = sqlite3.connect("../../data/sentiment.db")
    except Error as e:
        print(e)
        
    return connection


if __name__ == "__main__":
    conn = connect_db()

    conn.close()