import config
import pandas as pd
import requests
import pandas as pd
from datetime import datetime

apikey= config.API_KEY
base_url= config.base_url

# List of tickers to fetch news for
tickers = ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'GOOGL']

# Define date range (YYYY-MM-DD)
from_date = "2020-01-03"
to_date = "2025-03-21"

# Store all articles
all_articles = []


for ticker in tickers:
    url = f"{base_url}?symbol={ticker}&from={from_date}&to={to_date}&token={apikey}"
    response = requests.get(url)
    articles = response.json()

    for article in articles:
        all_articles.append({
            'ticker': ticker,
            'headline': article.get('headline'),
            'summary': article.get('summary'),
            'datetime': datetime.fromtimestamp(article['datetime']),
            'url': article.get('url'),
            'source': article.get('source')
        })

    print(f"{ticker} → {len(articles)} articles fetched")


# Convert to DataFrame
df = pd.DataFrame(all_articles)
print(df)