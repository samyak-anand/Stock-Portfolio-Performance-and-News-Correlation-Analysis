import pandas as pd
import news_injection
import stock_data_injection

# Suppress matplotlib logs
import logging
logging.getLogger('matplotlib').setLevel(logging.WARNING)

# Load data
portfolio = stock_data_injection.portfolio
portfolio_price = stock_data_injection.portfolio_price
news_data = news_injection.news_data

print("Loaded portfolio, portfolio_price, and news_data successfully.")

print(news_data.info())

# Drop 'Close' from portfolio
portfolio.drop('Close', axis=1, inplace=True)
print("'Close' column dropped from portfolio.")

portfolio.head()

# Drop 'url' from news_data
news_data.drop('url', axis=1, inplace=True)
print("'url' column dropped from news_data.")

print(news_data.head())

# Convert datetime to date in news dataset
news_data['datetime'] = pd.to_datetime(news_data['datetime'], errors='coerce').dt.date
news_data.rename(columns={'datetime': 'date'}, inplace=True)
news_data = news_data[['date', 'ticker', 'headline', 'summary', 'source']]
print("Datetime column processed and renamed to 'date' in news_data.")

# Dataframe overview function
def dataframe_overview(df):
    print('Dataframe Info:\n')
    df.info()

    print('\n Dataframe Description:\n')
    print(df.describe())
    
    print("\n Check null value in Dataframe: \n")
    print(df.isnull().sum())

    print('\n Check Duplicate values in Datafrme: \n')
    print(df.duplicated().sum())
    
    print('\n Check the unique values of dataframe: \n')
    print(df.nunique())

    print('\n Column Description: \n')
    print(list(df.columns))

    print('\n Shape of Dataframe (Rows,Colums):\n')
    print(df.shape)

    print('\n Data type of Each Column in Dataframe: \n ')
    print(df.dtypes)

    return

# Pass dataframes to overview
print('\n Displaying the Overview of Portfolio dataframe: \n')
dataframe_overview(portfolio)

print('\n Displaying the Overview of Portfolio Prices dataframe: \n')
dataframe_overview(portfolio_price)

print('\n Displaying the Overview of News dataframe: \n')
dataframe_overview(news_data)

# Cleaning function
def trim(df):
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')

    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.astype(str).str.strip())

    print("All column names cleaned, duplicates dropped, and text columns processed.")
    print("Clean dataset \n")
    print(df.head())
    return df

# Apply cleaning function
print("\n Clean Portfolio Dataset")
portfolio_df = trim(portfolio)
print("Portfolio dataset cleaned.")

print("\n Clean Portfolio Price Dataset")
portfolio_price_df = trim(portfolio_price)
print("Portfolio price dataset cleaned.")

print("\n Clean News Dataset")
news_data_df = trim(news_data)
print("News dataset cleaned.")

# Merge portfolio_price_df and portfolio_df
portfolio_merge = pd.merge(
    portfolio_price_df,
    portfolio_df,
    on=['ticker'],
    how="inner"
)

print("Portfolio merged successfully.")
print("Merge dataset: \n", portfolio_merge)

# Merge portfolio_merge and news_data_df
merge_df = pd.merge(
    portfolio_merge,
    news_data_df,
    on=['ticker', 'date'],
    how="inner"
)

print("Final merge with news data completed.")
print("Final merge dataset: \n", merge_df)
print(merge_df.info())
clean_merge_df= merge_df.copy()
# Text cleaning
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import string

custom_stopword = set(ENGLISH_STOP_WORDS)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^a-z\s]", '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[^a-zA-Z]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\b\w\b', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join(word for word in text.split() if len(word) >= 3)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\d+', '', text)

    words = text.split()
    filtered_words = [word for word in words if word not in custom_stopword]
    return ' '.join(filtered_words)

clean_merge_df['headline'] = clean_merge_df['headline'].apply(clean_text)
clean_merge_df['summary'] = clean_merge_df['summary'].apply(clean_text)
clean_merge_df['source'] = clean_merge_df['source'].apply(clean_text)

print("Text columns cleaned in final merged dataset.")

print("Final clean news_dataset: \n ", clean_merge_df)
print(clean_merge_df.info())
