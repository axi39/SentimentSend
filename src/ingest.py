### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020


import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
nltk.downloader.download('vader_lexicon')

#Global time variable, executes regardless of __name__ == "__main__"
timestamp = datetime.today().strftime('%Y-%m-%d-%H:%M')

def get_news(inlink, inheader):
    '''
    Scrape news site.

    parameter(s): news site URL (str), HTML header type for article titles (str)

    returns: articles from news site source (list)
    '''

    article_list = []

    response = requests.get(inlink)
    page = BeautifulSoup(response.text, "html.parser")

    titles = page.find_all(inheader)

    for title in titles:
        article_list.append(title.text)
    
    return article_list

def ingest_news(insource, inlink, inheader):
    '''
    Ingest news articles into DB

    parameter(s): news article source name (str), news site URL (str), HTML header type for article titles (str)

    returns: void.

    '''
    conn = sqlite3.connect('../data/sentiment.db')
    cursor = conn.cursor()

    #Setup sentiment capture.
    sia = SIA()
    senti = []

    #Call scraper.
    all_articles = get_news(inlink, inheader)

    #Insert scraped data and associated sentiment.
    for article in all_articles:
        score = sia.polarity_scores(article)
        cursor.execute("INSERT INTO Generalnews(source, title, date, sentiment) VALUES(?,?,?,?)", (insource, article, timestamp, float(score.get('compound'))))


    #Commit db changes and close db.
    conn.commit()
    conn.close()


if __name__ == "__main__":
    ingest_news("nyt", "https://www.nytimes.com/", "h2")
    ingest_news("bbc", "https://www.bbc.co.uk/news", "h3")