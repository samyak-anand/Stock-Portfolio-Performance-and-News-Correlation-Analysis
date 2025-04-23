import pandas as pd 



dow_jones_path='/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Dow_Jones.csv'
nasdaq_path= '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/NASDAQ.csv'
sp500_path = '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/SP500.csv'
portfolio_path= '/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio.csv'
portfolio_price_path='/home/samyak/PycharmProjects/Stock-Portfolio-Performance-and-News-Correlation-Analysis/Dataset/Portfolio_prices.csv'



dowjones=pd.read_csv(dow_jones_path)
nsadaq=pd.read_csv(nasdaq_path)
sp500=pd.read_csv(sp500_path)
portfolio = pd.read_csv(portfolio_path)
portfolio_price= pd.read_csv(portfolio_price_path)

print("Dow Jones \n ", dowjones)
print("NASDAQ \n ", nsadaq)
print("S&P 500 \n ", sp500)
print("Portfolio \n ", portfolio)
print("Portfolio Prices \n ", portfolio_price)