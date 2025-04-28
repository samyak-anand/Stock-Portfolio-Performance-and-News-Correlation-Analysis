# Configuration settings for the application

API_KEY = "d04gfqpr01qspgm2scagd04gfqpr01qspgm2scb0"
base_url = "https://finnhub.io/api/v1/company-news"

try:
    API_KEY = "d04gfqpr01qspgm2scagd04gfqpr01qspgm2scb0"  # Replace with your actual key
    base_url = "https://finnhub.io/api/v1/company-news"
    print("Configuration loaded successfully.")

except Exception as e:
    print(f"Error loading configuration: {e}")
