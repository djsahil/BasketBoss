import pandas
import warnings
import yfinance

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

def style_basic(styler):

    # Grid
    styler.set_properties(**{'border': '0.1px solid black'})

    # Remove index column
    styler.hide(axis='index')

    # Left justify some columns
    #styler.set_properties(subset=['Symbol', 'Name', 'Industry'], **{'text-align': 'left'})
    return styler

def calculate_metrics(ticker, start_date, end_date):
    # Fetch historical data
    stock_data = yfinance.download(ticker, start=start_date, end=end_date)

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
metrics_df = pandas.DataFrame(metrics_data)
metrics_df


df = yfinance.download(stocks, start=start_date)["Close"]

# Calculate Expected annualized returns
mu = expected_returns.mean_historical_return(df)
# Calculate annualized sample covariance matrix returns
S = risk_models.sample_cov(df)

# optimize for the MAX sharpe ratio
# create the efficient frontier object
efficient_frontier = EfficientFrontier(mu, S)
weights = efficient_frontier.max_sharpe()

#round small marginal weights to 0
cleaned_weights = efficient_frontier.clean_weights()

cleaned_weights_df = pandas.DataFrame([cleaned_weights])
cleaned_weights_df
efficient_frontier.portfolio_performance(verbose=True)

# get the discrete allocation of each share per stock
# your budget for investing
my_budget = 250000
latest_prices = get_latest_prices(df)
weights = cleaned_weights
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=my_budget)
allocation, leftover = da.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining:", "$", leftover)

# Style Dataframe
(metrics_df.style.pipe(style_basic)
    .set_caption('Historical Performance Metrics')
    .set_table_styles(
    [{
        'selector': 'th.col_heading',
        'props': 'text-align: center'
    }, {
        'selector': 'caption',
        'props': [('text-align', 'center'),
                  ('font-size', '14pt'),
                  ('font-weight', 'bold')]}
    ]))
