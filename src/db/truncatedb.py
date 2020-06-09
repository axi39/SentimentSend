### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020

import sqlite3
from sqlite3 import Error


def truncate_table(db_con, in_table):
    '''
    Truncates single db table

    parameter(s): db_con (connection object), int_table (db table object)

    returns: void
    '''
    try:
        cursor = db_con.cursor()

        truncate_statement = 'DELETE FROM ' + in_table + ' IF EXISTS;'

        cursor.execute(truncate_statement)

    except Error as e:
        print(e)



def truncate_tables(db_con, in_tables):
    '''
    Truncates all DB tables

    parameter(s): db_con (connection object), in_table (list of in_tables (db table object))

    returns: void
    '''
    try:
        cursor = db_con.cursor()

        for table in in_tables
            truncate_statement = 'DELETE FROM ' + table + ' IF EXISTS;'

            cursor.execute(truncate_statement)
        #for table in cursor.execute('SELECT name FROM sqlite_master WHERE type = "table" ORDER BY name').fetchall():
        ## SQLite does not accept string formatting on tables or databases.  Should use parametrization when refactoring.
        ## Assuming SQL injection prevention has has something to do with this.
        #    cursor.execute('DELETE FROM ' + str(table) + ' ;')
    except Error as e:
        print(e)


if __name__ == "__main__":
    connection = sqlite3.connect("../../data/sentiment.db")

    tables = ['Generalnews', 'Tickernews', 'Tickerprices']

    truncate_tables(connection)

    connection.commit()
    connection.close()