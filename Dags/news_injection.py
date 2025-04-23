import config
import pandas as pd
import requests
from datetime import datetime
from logger import logger  # Import the central logger

logger.info("Starting data injection process...")

apikey = config.API_KEY
base_url = config.base_url

# List of tickers to fetch news for
tickers = ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'GOOGL']

# Define date range (YYYY-MM-DD)
from_date = "2020-01-03"
to_date = "2025-03-21"

# Store all articles
all_articles = []

try:
    for ticker in tickers:
        logger.info(f"Fetching news for {ticker}")
        url = f"{base_url}?symbol={ticker}&from={from_date}&to={to_date}&token={apikey}"
        response = requests.get(url)
        response.raise_for_status()  # Handle HTTP errors
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

        logger.info(f"{ticker} → {len(articles)} articles fetched")

    # Convert to DataFrame
    df = pd.DataFrame(all_articles)
    logger.info("Converted articles to DataFrame successfully")
    logger.debug(df.head())  # Optional preview

    print(df)  # Retaining print since it was in original code

except requests.exceptions.RequestException as req_err:
    logger.error(f"HTTP Request failed: {req_err}", exc_info=True)
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}", exc_info=True)
