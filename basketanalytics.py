import yfinance as yf
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def fetch_stock_info(ticker):
    # GET Yahoo Finance TICKER INFO
    yfTicker = yf.Ticker(ticker)
    stock_info = yfTicker.info
    print(stock_info)
    print("\033[4m", stock_info['symbol'], "(", stock_info['shortName'], ")\033[0m", sep='')
    print("Historical Revenue Growth:", stock_info['revenueGrowth'])
    print("Forward P/E Ratio:", stock_info['forwardPE'])
    #print("Debt to Equity Ratio:", stock_info['debtToEquity'])
    #print("Quick Ratio:", stock_info['quickRatio'])
    print("Return on Equity:", stock_info['returnOnEquity'])
    print("Return on Assets:", stock_info['returnOnAssets'])
    print('\n')

    # EXTRACT historical data, yf.download() for data range
    # historical_data = yf.download(ticker, start="2000-01-01", end="2023-01-01")
    historical_data = yfTicker.history(period="max")

    #print(yfTicker.news)


stocks = ['AAPL', 'GS', 'IBM', 'INTC', 'JNJ', 'JPM', 'MS', 'TRV']
for ticker in stocks:
    fetch_stock_info(ticker)
