import pandas as pd

# File paths
dow_jones_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Dow_Jones.csv'
nasdaq_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/NASDAQ.csv'
sp500_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/SP500.csv'
portfolio_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio.csv'
portfolio_price_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio_prices.csv'

# Load datasets with print statements instead of logging
try:
    dowjones = pd.read_csv(dow_jones_path)
    print("Dow Jones data loaded successfully.")
except Exception as e:
    print(f"Failed to load Dow Jones data: {e}")

try:
    nsadaq = pd.read_csv(nasdaq_path)
    print("NASDAQ data loaded successfully.")
except Exception as e:
    print(f"Failed to load NASDAQ data: {e}")

try:
    sp500 = pd.read_csv(sp500_path)
    print("S&P 500 data loaded successfully.")
except Exception as e:
    print(f"Failed to load S&P 500 data: {e}")

try:
    portfolio = pd.read_csv(portfolio_path)
    print("Portfolio data loaded successfully.")
except Exception as e:
    print(f"Failed to load Portfolio data: {e}")

try:
    portfolio_price = pd.read_csv(portfolio_price_path)
    print("Portfolio prices data loaded successfully.")
except Exception as e:
    print(f"Failed to load Portfolio prices data: {e}")

# Print the head of each DataFrame to verify their content
print("Dow Jones \n", dowjones.head() if 'dowjones' in locals() else 'Dow Jones not loaded')
print("NASDAQ \n", nsadaq.head() if 'nsadaq' in locals() else 'NASDAQ not loaded')
print("S&P 500 \n", sp500.head() if 'sp500' in locals() else 'S&P 500 not loaded')
print("Portfolio \n", portfolio.head() if 'portfolio' in locals() else 'Portfolio not loaded')
print("Portfolio Prices \n", portfolio_price.head() if 'portfolio_price' in locals() else 'Portfolio Prices not loaded')
