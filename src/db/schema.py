### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020


import sqlite3
from sqlite3 import Error
import createdb as cd  


def create_table(table, db_con):
    '''
    Creates tables in SQLite DB file.

    parameter(s): table (str), db_con (connection object)

    returns: void
    '''

    try:
        cursor = db_con.cursor()
        cursor.execute(table)
    except Error as e:
        print(e)

if __name__ == "__main__":

    conn = sqlite3.connect("../../data/sentiment.db")

    general_news_table = '''CREATE TABLE IF NOT EXISTS Generalnews(
                    id INTEGER PRIMARY KEY,
                    source TEXT NOT NULL,
                    title TEXT NOT NULL UNIQUE ON CONFLICT IGNORE,
                    date TEXT NOT NULL,
                    sentiment REAL
                    );'''

    ticker_news_table = '''CREATE TABLE IF NOT EXISTS Tickernews(
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL UNIQUE ON CONFLICT IGNORE,
                    date TEXT NOT NULL,
                    sentiment REAL
                    );'''
    
    ticker_price_table = '''CREATE TABLE IF NOT EXISTS Tickerprices(
                    id INTEGER PRIMARY KEY,
                    ticker TEXT NOT NULL,
                    date TEXT NOT NULL,
                    close REAL NOT NULL
                    );'''
    

    #Create defined tables
    create_table(general_news_table, conn)
    create_table(ticker_news_table, conn)
    create_table(ticker_price_table, conn)

    conn.commit()

    conn.close()

