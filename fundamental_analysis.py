import yfinance
import pandas
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def style_fundamentals_dataframe(styler):
    # Column formatting
    styler.format({'Forward Earnings Per Share (EPS)': '${:.2f}', 'Forward Price to Earnings Ratio (P/E)': '{:.2f}',
                   'Price/Earnings-to-Growth Ratio (PEG)': '{:.2f}',
                   'FCFY': '{:.2f}%', 'Price to Book Ratio (P/B)': '{:.2f}', 'Return on Equity (ROE)': '{:.2f}',
                   '12-Month Trailing Price-to-Sales Ratio (P/S)': '{:.2f}',
                   'Dividend Payout Ratio (DPR)': '{:.2f}%', 'Dividend Yield (DY)': '{:.2f}%',
                   'Current Ratio (CR)': '{:.2f}', 'Beta': '{:.2f}', '52-Week Low': '${:.2f}',
                   'Price': '${:.2f}', '52-Week High': '${:.2f}'})

    # Grid
    styler.set_properties(**{'border': '0.1px solid black'})

    # Set background gradients
    styler.background_gradient(subset=['Forward Earnings Per Share (EPS)'], cmap='Greens')
    styler.background_gradient(subset=['Forward Price to Earnings Ratio (P/E)'], cmap='Greens')
    styler.background_gradient(subset=['Price/Earnings-to-Growth Ratio (PEG)'], cmap='Greens')
    # styler.background_gradient(subset=['FCFY'], cmap='Greens')
    styler.background_gradient(subset=['Price to Book Ratio (P/B)'], cmap='Greens')
    styler.background_gradient(subset=['Return on Equity (ROE)'], cmap='Greens')
    styler.background_gradient(subset=['12-Month Trailing Price-to-Sales Ratio (P/S)'], cmap='Greens')
    styler.background_gradient(subset=['Dividend Payout Ratio (DPR)'], cmap='Greens')
    styler.background_gradient(subset=['Dividend Yield (DY)'], cmap='Greens')
    # styler.background_gradient(subset=['Current Ratio (CR)'], cmap='Greens')

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
        # 'Free Cash Flow Yield (FCFY)': []],
        'Price to Book Ratio (P/B)': [],
        'Return on Equity (ROE)': [],
        '12-Month Trailing Price-to-Sales Ratio (P/S)': [],
        'Dividend Payout Ratio (DPR)': [],
        'Dividend Yield (DY)': [],
        # 'Current Ratio (CR)': []],
        'Beta': [],
        'Price': [],
        '52-Week Low': [],
        '52-Week High': []
    }

    for ticker in stocks:
        # GET Yahoo Finance TICKER INFO
        yfTicker = yfinance.Ticker(ticker)
        stock_info = yfTicker.info

        stock_data['Symbol'].append(stock_info['symbol'])
        stock_data['Name'].append(stock_info['shortName'])
        stock_data['Industry'].append(stock_info['industry'])
        stock_data['Forward Earnings Per Share (EPS)'].append(stock_info['forwardEps'])
        stock_data['Forward Price to Earnings Ratio (P/E)'].append(stock_info['forwardPE'])
        stock_data['Price/Earnings-to-Growth Ratio (PEG)'].append(stock_info['pegRatio'])
        # stock_data['Free Cash Flow Yield (FCFY)'].append(stock_info['freeCashflow'])
        stock_data['Price to Book Ratio (P/B)'].append(stock_info['priceToBook'])
        stock_data['Return on Equity (ROE)'].append(stock_info['returnOnEquity'])
        stock_data['12-Month Trailing Price-to-Sales Ratio (P/S)'].append(stock_info['priceToSalesTrailing12Months'])
        stock_data['Dividend Payout Ratio (DPR)'].append(stock_info['payoutRatio'])
        stock_data['Dividend Yield (DY)'].append(stock_info['dividendYield'])
        # stock_data['Current Ratio (CR)'].append(stock_info['currentRatio'])
        stock_data['Beta'].append(stock_info['beta'])
        stock_data['Price'].append(stock_info['currentPrice'])
        stock_data['52-Week Low'].append(stock_info['fiftyTwoWeekLow'])
        stock_data['52-Week High'].append(stock_info['fiftyTwoWeekHigh'])

    # Return a DF using the stock_data dictionary
    return pandas.DataFrame(stock_data)


stocks = ['AAPL', 'GS', 'IBM', 'INTC', 'JNJ', 'JPM', 'MS', 'TRV']
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
                  ('font-size', '10pt'),
                  ('font-weight', 'bold')]}
    ])
