import pandas as pd
from logger import logger  

# File paths
dow_jones_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Dow_Jones.csv'
nasdaq_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/NASDAQ.csv'
sp500_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/SP500.csv'
portfolio_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio.csv'
portfolio_price_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio_prices.csv'

# Load datasets with logging
try:
    dowjones = pd.read_csv(dow_jones_path)
    logger.info("Dow Jones data loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load Dow Jones data: {e}", exc_info=True)

try:
    nsadaq = pd.read_csv(nasdaq_path)
    logger.info("NASDAQ data loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load NASDAQ data: {e}", exc_info=True)

try:
    sp500 = pd.read_csv(sp500_path)
    logger.info("S&P 500 data loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load S&P 500 data: {e}", exc_info=True)

try:
    portfolio = pd.read_csv(portfolio_path)
    logger.info("Portfolio data loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load Portfolio data: {e}", exc_info=True)

try:
    portfolio_price = pd.read_csv(portfolio_price_path)
    logger.info("Portfolio prices data loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load Portfolio prices data: {e}", exc_info=True)

# Optional preview (keep or comment out)
logger.debug("Dow Jones \n%s", dowjones.head() if 'dowjones' in locals() else 'Dow Jones not loaded')
logger.debug("NASDAQ \n%s", nsadaq.head() if 'nsadaq' in locals() else 'NASDAQ not loaded')
logger.debug("S&P 500 \n%s", sp500.head() if 'sp500' in locals() else 'S&P 500 not loaded')
logger.debug("Portfolio \n%s", portfolio.head() if 'portfolio' in locals() else 'Portfolio not loaded')
logger.debug("Portfolio Prices \n%s", portfolio_price.head() if 'portfolio_price' in locals() else 'Portfolio Prices not loaded')
