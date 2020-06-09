### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#IN PROGRESS, 04.06.2020

import server 
import ingest_ticker as it 


if __name__ == "__main__":


    server.app.run(debug=True)

    if it.get_ingest_ticker_price():
        pass
    else:
        pass

    


    