# Configuration settings for the application
#API key 


from logger import logger

def function_one():
    logger.info("Function One called")


API_KEY = "d04gfqpr01qspgm2scagd04gfqpr01qspgm2scb0"
base_url = "https://finnhub.io/api/v1/company-news"

import logging

# Optional: configure local logging for config-related events
logger = logging.getLogger('StockPortfolioLogger')

try:
    API_KEY = "d04gfqpr01qspgm2scagd04gfqpr01qspgm2scb0"  # Replace with your actual key
    base_url = "https://finnhub.io/api/v1/company-news"

    logger.info("Configuration loaded successfully.")

except Exception as e:
    logger.error(f"Error loading configuration: {e}", exc_info=True)
