import yfinance as yf
import pandas as pd

def calculate_metrics(ticker, start_date, end_date):
    # Fetch historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

    # Calculate volatility (annualized standard deviation of daily returns)
    volatility = stock_data['Daily_Return'].std() * (252 ** 0.5)

    # Calculate cumulative returns
    cumulative_returns = (1 + stock_data['Daily_Return']).cumprod() - 1

    # Calculate drawdowns
    cumulative_max = cumulative_returns.cummax()
    drawdowns = (cumulative_returns - cumulative_max) / (cumulative_max + 1)

    # Calculate metrics
    total_return = cumulative_returns.iloc[-1]
    max_drawdown = drawdowns.min()
    avg_annual_return = cumulative_returns.mean() * 252
    sharpe_ratio = avg_annual_return / volatility

    return {
        'Ticker': ticker,
        'Total Return': total_return,
        'Volatility': volatility,
        'Max Drawdown': max_drawdown,
        'Average Annual Return': avg_annual_return,
        'Sharpe Ratio': sharpe_ratio
    }

# Example usage
stocks = ['AAPL', 'GS', 'IBM', 'INTC', 'JNJ', 'JPM', 'MS', 'TRV', 'GOOG', 'TSLA']
start_date = '2019-01-01'
end_date = '2022-01-01'

metrics_data = []
for ticker in stocks:
    metrics = calculate_metrics(ticker, start_date, end_date)
    metrics_data.append(metrics)

# Create a DataFrame to display results
metrics_df = pd.DataFrame(metrics_data)
print(metrics_df)
