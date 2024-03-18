import yfinance
import pandas
import numpy
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def style_fundamentals_dataframe(styler):
    # Column formatting
    styler.format({'Forward Earnings Per Share (EPS)': '${:.2f}', 'Forward Price to Earnings Ratio (P/E)': '{:.2f}',
                   'Price/Earnings-to-Growth Ratio (PEG)': '{:.2f}',
                   'Free Cash Flow Yield (FCFY)': '{:.2f}', 'Price to Book Ratio (P/B)': '{:.2f}', 'Return on Equity (ROE)': '{:.2f}',
                   '12-Month Trailing Price-to-Sales Ratio (P/S)': '{:.2f}',
                   'Dividend Payout Ratio (DPR)': '{:.2f}', 'Dividend Yield (DY)': '{:.2f}%',
                   'Current Ratio (CR)': '{:.2f}', 'Beta': '{:.2f}', '52-Week Low': '${:.2f}',
                   'Price': '${:.2f}', '52-Week High': '${:.2f}'})

    # Grid
    styler.set_properties(**{'border': '0.1px solid black'})

    # Set background gradients
    styler.background_gradient(subset=['Forward Earnings Per Share (EPS)'], cmap='Greens')
    styler.background_gradient(subset=['Forward Price to Earnings Ratio (P/E)'], cmap='Greens')
    styler.background_gradient(subset=['Price/Earnings-to-Growth Ratio (PEG)'], cmap='Greens')
    styler.background_gradient(subset=['Price to Book Ratio (P/B)'], cmap='Greens')
    styler.background_gradient(subset=['Return on Equity (ROE)'], cmap='Greens')
    styler.background_gradient(subset=['12-Month Trailing Price-to-Sales Ratio (P/S)'], cmap='Greens')
    styler.background_gradient(subset=['Dividend Payout Ratio (DPR)'], cmap='Greens')
    styler.background_gradient(subset=['Dividend Yield (DY)'], cmap='Greens')
    styler.background_gradient(subset=['Current Ratio (CR)'], cmap='Greens')

    # Remove index column
    styler.hide(axis='index')

    # Left justify some columns
    styler.set_properties(subset=['Symbol', 'Name', 'Industry'], **{'text-align': 'left'})
    return styler

def fetch_stock_info(stocks):
    stock_data = {
        'Symbol': [],
        'Name': [],
        'Industry': [],
        'Forward Earnings Per Share (EPS)': [],
        'Forward Price to Earnings Ratio (P/E)': [],
        'Price/Earnings-to-Growth Ratio (PEG)': [],
        'Price to Book Ratio (P/B)': [],
        'Return on Equity (ROE)': [],
        '12-Month Trailing Price-to-Sales Ratio (P/S)': [],
        'Dividend Payout Ratio (DPR)': [],
        'Dividend Yield (DY)': [],
        'Current Ratio (CR)': [],
        'Free Cash Flow Yield (FCFY)': [],
        'Beta': [],
        'Price': [],
        '52-Week Low': [],
        '52-Week High': []
    }

    key_yfinancekey_map = {
        'Symbol': 'symbol',
        'Name': 'shortName',
        'Industry': 'industry',
        'Forward Earnings Per Share (EPS)': 'forwardEps',
        'Forward Price to Earnings Ratio (P/E)': 'forwardPE',
        'Price/Earnings-to-Growth Ratio (PEG)': 'pegRatio',
        'Price to Book Ratio (P/B)': 'priceToBook',
        'Return on Equity (ROE)': 'returnOnEquity',
        '12-Month Trailing Price-to-Sales Ratio (P/S)': 'priceToSalesTrailing12Months',
        'Dividend Payout Ratio (DPR)': 'payoutRatio',
        'Dividend Yield (DY)': 'dividendYield',
        'Current Ratio (CR)': 'currentRatio',
        'Free Cash Flow Yield (FCFY)': 'freeCashflow',
        'Beta': 'beta',
        'Price': 'currentPrice',
        '52-Week Low': 'fiftyTwoWeekLow',
        '52-Week High': 'fiftyTwoWeekHigh'
    }

    key_list = stock_data.keys()


    for ticker in stocks:
        # GET Yahoo Finance TICKER INFO
        yfTicker = yfinance.Ticker(ticker)
        stock_info = yfTicker.info


        for stock_data_key in key_list:
            try:
                stock_data[stock_data_key].append(stock_info[key_yfinancekey_map[stock_data_key]])
            except KeyError:
                stock_data[stock_data_key].append(numpy.nan)

    # Return a DF using the stock_data dictionary
    return pandas.DataFrame(stock_data)


stocks = ['AAPL', 'GS', 'IBM', 'INTC', 'JNJ', 'JPM', 'MS', 'TRV', 'GOOG']
stock_info_dataframe = fetch_stock_info(stocks)
# print(stock_info_dataframe)

# Style Dataframe
stock_info_dataframe.style.pipe(style_fundamentals_dataframe).set_caption('Fundamental Analysis Indicators').set_table_styles(
    [{
        'selector': 'th.col_heading',
        'props': 'text-align: center'
    }, {
        'selector': 'caption',
        'props': [('text-align', 'center'),
                  ('font-size', '14pt'),
                  ('font-weight', 'bold')]}
    ])
