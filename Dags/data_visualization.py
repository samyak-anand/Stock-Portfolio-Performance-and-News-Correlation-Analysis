## data visualization 

import prepare_dataset
import pandas as pd
import matplotlib.pyplot as plt

df= prepare_dataset.merge_df

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'date': pd.date_range(start='2024-01-01', periods=100),
    'adjusted': range(100)
})

# Group by date and compute average adjusted price
avg_prices = df.groupby("date")["adjusted"].mean().reset_index()

# Create the plot
plt.figure(figsize=(16, 8))
plt.plot(avg_prices["date"], avg_prices["adjusted"], color='red', linewidth=2)

# Customize the plot
plt.title("Average Portfolio Adjusted Prices Over Time", fontsize=18)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Average Adjusted Price", fontsize=14)
plt.grid(True)
plt.tight_layout()

# Show the plot interactively
plt.show()



import matplotlib.pyplot as plt

# Count the frequency of each ticker
ticker_count = df['ticker'].value_counts().reset_index()
ticker_count.columns = ['ticker', 'count']

# Create the bar plot
plt.figure(figsize=(14, 6))
bars = plt.bar(ticker_count['ticker'], ticker_count['count'], color='blue')

# Add titles and labels
plt.title("Ticker Count in Portfolio Merge Dataset", fontsize=16)
plt.xlabel("Ticker", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Add integer count labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f"{int(height)}",
             ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
display(plt.gcf())


avg_sec_price =df.groupby('sector')['adjusted'].mean().sort_values(ascending=False)
avg_sec_price.plot(kind='bar', figsize=(12, 6), color='green')
plt.title("Average Adjusted Price by Sector")
plt.ylabel("Average Adjusted Price")

# Add count labels on top of bars with 2 decimal places
for i, count in enumerate(avg_sec_price):
    plt.text(i, count + 0.02 * max(avg_sec_price), f"{count:.2f}", ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



df.groupby("sector")["weight"].sum().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), startangle=90)
plt.title("Portfolio Weight Distribution by Sector")
plt.ylabel("ff")  
plt.show()


from wordcloud import WordCloud 
def plot_ticker_and_news_visualization(df):
    df['ticker']= df['ticker'].astype(str)
    df['headline']= df['headline'].astype(str)
    df['summary'] =df['summary'].astype(str)

    # Word Cloud of Ticker Mentions
    ticker_text = ' '.join(df['ticker'])
    ticker_wordcloud = WordCloud(background_color='white', width=800, height=400).generate(ticker_text)

    plt.figure(figsize=(12, 8))
    plt.imshow(ticker_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Ticker Mentions in Headline")
    plt.show()


    # Word Cloud of All Tweets
    all_headline_text = ' '.join(df['headline'])
    headline_wordcloud = WordCloud(background_color='white', width=800, height=400, max_words=200, colormap='viridis').generate(all_headline_text)

    plt.figure(figsize=(12, 8))
    plt.imshow(headline_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of All Headline")
    plt.show()

    # Word Cloud of All Tweets
    all_summary_text = ' '.join(df['headline'])
    summary_wordcloud = WordCloud(background_color='white', width=800, height=400, max_words=200, colormap='viridis').generate(all_summary_text)

    plt.figure(figsize=(12, 8))
    plt.imshow(summary_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of All Summary")
    plt.show()
    #Bar Plot: Total Word Count of Headline Per Ticker
    df['word_count'] = df['headline'].apply(lambda x: len(x.split()))
    total_word_count_per_ticker = df.groupby('ticker')['word_count'].sum().sort_values(ascending=False)

    plt.figure(figsize=(14, 8))
    plt.bar(total_word_count_per_ticker.index, total_word_count_per_ticker, color='skyblue')
    plt.title('Total Word Count of Headline per Ticker')
    # Add count labels on top of bars
    for i, count in enumerate(total_word_count_per_ticker):
        plt.text(i, count + 0.02 * max(total_word_count_per_ticker), str(count), ha='center', va='bottom', fontsize=8)

    plt.xticks(rotation=45)
    plt.xlabel('Ticker')
    plt.ylabel('Total Word Count')

     #Bar Plot: Total Word Count of Summary Per Ticker
    df['word_count'] = df['summary'].apply(lambda x: len(x.split()))
    total_word_count_per_ticker = df.groupby('ticker')['word_count'].sum().sort_values(ascending=False)

    plt.figure(figsize=(14, 8))
    plt.bar(total_word_count_per_ticker.index, total_word_count_per_ticker, color='skyblue')
    plt.title('Total Word Count of summary per Ticker')

    # Add count labels on top of bars
    for i, count in enumerate(total_word_count_per_ticker):
        plt.text(i, count + 0.02 * max(total_word_count_per_ticker), str(count), ha='center', va='bottom', fontsize=8)

    plt.xticks(rotation=45)
    plt.xlabel('Ticker')
    plt.ylabel('Total Word Count')



# Resample tweets by day to analyze volume over time
# Convert 'Date' column to DatetimeIndex and set it as index
df['date'] = pd.to_datetime(df['date'])  # Convert 'Date' to datetime objects
df.set_index('date', inplace=True)            # Set 'Date' column as the index

# Now you can apply resample
tweet_volume = df.resample("d").size()

# Plot
plt.figure(figsize=(16, 6))
plt.plot(tweet_volume.index, tweet_volume.values, marker="o", linestyle="-", color="b")
plt.xlabel("Date")
plt.ylabel("News Volume")
plt.title("News Volume Over Time")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
