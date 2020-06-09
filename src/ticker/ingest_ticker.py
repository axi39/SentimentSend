### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020

import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
nltk.downloader.download('vader_lexicon')
from alpha_vantage.techindicators import TechIndicators
import senderror as se

#Global time variable, executes regardless of __name__ == "__main__"
timestamp = datetime.today().strftime('%Y-%m-%d-%H:%M')


def get_ticker_article(inticker):
    '''
    Scrape news articles pertaining to ticker.

    parameter(s): stock ticker (str)

    returns: articles from news site source (list)
    '''

    stories_list = []

    #Utilizes Google News for search parameters on ticker.
    link = "https://news.google.com/search?q=" + inticker + "'" + timestamp + "'"

    try:
        response = requests.get(link)
    except requests.exceptions.RequestException as e:
        return e

    page = BeautifulSoup(response.text, "html.parser")

    stories = page.find_all("h3")

    for story in stories[:5]:

        stories_list.append(story.text)
    
    return stories_list


def ingest_ticker_article(inticker, date):
    '''
    Load ticker related articles into DB.

    parameter(s): stock ticker (str), timestamp (datetime)

    returns: void
    '''

    #Setup sentiment capture.
    sia = SIA()
    senti = []

    all_articles = get_ticker_article(inticker)

    for article in all_articles:
        #Append NLP scores to articles.
        score = sia.polarity_scores(article)
        cursor.execute("INSERT INTO Tickernews(title, date, sentiment) VALUES(?,?,?,?)", (article, timestamp, float(score.get('compound'))))

    

def get_ingest_ticker_price(inticker):
    '''
    Load AlphaVantage stock data into DB

    parameter(s): stock (str)

    returns: void
    '''
    conn = sqlite3.connect('../../data/sentiment.db')
    cursor = conn.cursor()


    try:
        ts = TechIndicators(key='INSERTKEY', output_format='pandas')
        data, meta_data = ts.get_sma(symbol=inticker,interval='60min', time_period = 32, series_type = 'close')
        for row in data:
            cursor.execute("INSERT INTO Tickerprices(ticker, date, close) VALUES(?,?,?)", (inticker, timestamp, row))
        return True
    except:
        se.send_ticker_error()
        return False


if __name__ == "__main__":
    
    #FUNCTION -> ingest_ticker_article:  Correct input.
    #ingest_ticker_article("MSFT", timestamp)

    #FUNCTION -> get_ingest_ticker_price:  Incorrect input.
    get_ingest_ticker_price("MisoSoup")