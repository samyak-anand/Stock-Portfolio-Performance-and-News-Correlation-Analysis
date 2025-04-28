import config
import pandas as pd
import requests
from datetime import datetime

# Print information instead of using logger
print("Starting data injection process...")

apikey = config.API_KEY
base_url = config.base_url

# List of tickers to fetch news for
tickers = ['AAPL', 'ADAP', 'AGCO', 'BA', 'BG', 'CALM', 'CAT', 'CSCO', 'CVX',
       'DDOG', 'DE', 'GRWG', 'HUM', 'IBKR', 'IEX', 'JPM', 'KO', 'LMT',
       'MS', 'MSCI', 'MSFT', 'NFLX', 'OSK', 'PFE', 'PG', 'SPY', 'TMUS','GSPC','IXIC']

# Define date range (YYYY-MM-DD)
from_date = "2020-01-03"
to_date = "2025-03-21"

# Store all articles
all_articles = []

try:
    for ticker in tickers:
        print(f"Fetching news for {ticker}")
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

        print(f"{ticker} → {len(articles)} articles fetched")

    # Convert to DataFrame
    df = pd.DataFrame(all_articles)
    print("Converted articles to DataFrame successfully")
    print(df.head())  # Print the first few rows to verify

    print(df)  # Retaining print since it was in original code

except requests.exceptions.RequestException as req_err:
    print(f"HTTP Request failed: {req_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# To save the data into .csv file
output_file = 'updated_news_data.csv'
df.to_csv(output_file, index=False)
print(f"Stock data saved to '{output_file}'")

# Loading the saved CSV to verify data
news_data = pd.read_csv('updated_news_data.csv')
