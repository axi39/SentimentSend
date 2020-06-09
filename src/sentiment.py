### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020


import pandas as pd
import sqlite3
from sqlite3 import Error



def clean():
    '''
    Cleans data for SMS send

    parameter(s): none.

    returns: sentiment aggregate scores grouped by script run (Pandas dataframe)

    '''
    con = sqlite3.connect("../data/sentiment.db")
    cur = con.cursor()

    #Load source
    df_bbc = pd.read_sql_query("SELECT * FROM Generalnews WHERE source = 'bbc'", con)
    df_nyt = pd.read_sql_query("SELECT * FROM Generalnews WHERE source = 'nyt'", con)

    #Remove tail 3 rows of BBC ingest timestamp instance data.  Only applicable if multiple runs in one day.
    trim_bbc = df_bbc.groupby('date', as_index = False).apply(lambda x: x[0:-3])

    #Remove head 3 and tail 3 NYT ingest timestamp instance data.  Only applicable if multiple runs in one day.
    trim_nyt = df_bbc.groupby('date', as_index = False).apply(lambda x: x[2:-3])

    #Union datasets from sources
    trim_total = pd.concat([trim_bbc, trim_nyt])

    return trim_total

    #Get mean sentiment for dates
    grouped_means = trim_total.groupby([pd.to_datetime(trim_total.date)])['sentiment'].mean().reset_index()
    #return grouped_means
    
if __name__ == "__main__":
    print(clean())
    