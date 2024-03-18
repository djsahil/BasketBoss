import yfinance
import json
import jinja2
# For DataFrame
import pandas
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def make_pretty(styler):
    # Column formatting
    styler.format({'Forward Earnings Per Share (EPS)': '${:.2f}', 'P/E (fwd)': '{:.2f}', 'PEG': '{:.2f}',
                   'FCFY': '{:.2f}%', 'PB' : '{:.2f}', 'ROE' : '{:.2f}', 'P/S (trail)': '{:.2f}',
                   'DPR': '{:.2f}%', 'DY': '{:.2f}%', 'CR' : '{:.2f}', 'Beta': '{:.2f}', '52w Low': '${:.2f}',
                   'Price': '${:.2f}', '52w High': '${:.2f}', '52w Range': '{:.2f}%'
                  })
    # Set the bar visualization
    styler.bar(subset = ['52w Range'], align = "mid", color = ["salmon", "cornflowerblue"])

    # Grid
    styler.set_properties(**{'border': '0.1px solid black'})

    # Set background gradients
    styler.background_gradient(subset=['Forward Earnings Per Share (EPS)'], cmap='Greens')
    styler.background_gradient(subset=['P/E (fwd)'], cmap='Greens')
    styler.background_gradient(subset=['PEG'], cmap='Greens')
    styler.background_gradient(subset=['FCFY'], cmap='Greens')
    styler.background_gradient(subset=['PB'], cmap='Greens')
    styler.background_gradient(subset=['ROE'], cmap='Greens')
    styler.background_gradient(subset=['P/S (trail)'], cmap='Greens')
    styler.background_gradient(subset=['DPR'], cmap='Greens')
    styler.background_gradient(subset=['DY'], cmap='Greens')
    styler.background_gradient(subset=['CR'], cmap='Greens')

    # No index
    styler.hide(axis='index')

    # Tooltips
    '''
    styler.set_tooltips(
        ttips, css_class='tt-add',
        props=[
            ('visibility', 'hidden'),
            ('position', 'absolute'),
            ('background-color', 'salmon'),
            ('color', 'black'),
            ('z-index', 1),
            ('padding', '3px 3px'),
            ('margin', '2px')
        ]
    )
    '''
    # Left text alignment for some columns
    styler.set_properties(subset=['Symbol', 'Name', 'Industry'], **{'text-align': 'left'})
    return styler


def populate_tt(df, tt_data, col_name):
    stats = df[col_name].describe()

    per25 = round(stats.loc['25%'], 2)
    per50 = round(stats.loc['50%'], 2)
    per75 = round(stats.loc['75%'], 2)

    # Get position based on the column name
    pos = df.columns.to_list().index(col_name)

    for index, row in df.iterrows():
        pe = row[col_name]
        if pe == stats.loc['min']:
            tt_data[index][pos] = 'Lowest'
        elif pe == stats.loc['max']:
            tt_data[index][pos] = 'Hightest'
        elif pe <= per25:
            tt_data[index][pos] = '25% of companies under {}'.format(per25)
        elif pe <= per50:
            tt_data[index][pos] = '50% of companies under {}'.format(per50)
        elif pe <= per75:
            tt_data[index][pos] = '75% of companies under {}'.format(per75)
        else:
            tt_data[index][pos] = '25% of companies over {}'.format(per75)
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
        #stock_data['Free Cash Flow Yield (FCFY)'].append(stock_info['freeCashflow'])
        stock_data['Price to Book Ratio (P/B)'].append(stock_info['priceToBook'])
        stock_data['Return on Equity (ROE)'].append(stock_info['returnOnEquity'])
        stock_data['12-Month Trailing Price-to-Sales Ratio (P/S)'].append(stock_info['priceToSalesTrailing12Months'])
        stock_data['Dividend Payout Ratio (DPR)'].append(stock_info['payoutRatio'])
        stock_data['Dividend Yield (DY)'].append(stock_info['dividendYield'])
        #stock_data['Current Ratio (CR)'].append(stock_info['currentRatio'])
        stock_data['Beta'].append(stock_info['beta'])
        stock_data['Price'].append(stock_info['currentPrice'])
        stock_data['52-Week Low'].append(stock_info['fiftyTwoWeekLow'])
        stock_data['52-Week High'].append(stock_info['fiftyTwoWeekHigh'])

    # Return a DF using the stock_data dictionary
    return pandas.DataFrame(stock_data)


stocks = ['AAPL', 'GS', 'IBM', 'INTC', 'JNJ', 'JPM', 'MS', 'TRV']
stock_info_dataframe = fetch_stock_info(stocks)
print(stock_info_dataframe)

# Initialize tool tip data - each column is set to '' for each row
tt_data = [['' for x in range(len(stock_info_dataframe.columns))] for y in range(len(stock_info_dataframe))]

# Gather tool tip data for indicators
populate_tt(stock_info_dataframe, tt_data, 'Symbol')
#populate_tt(stock_info_dataframe, tt_data, 'Name')
#populate_tt(stock_info_dataframe, tt_data, 'Industry')


# Create a tool tip DF
#ttips = stock_info_dataframe.DataFrame(data=tt_data, columns=stock_info_dataframe.columns, index=stock_info_dataframe.index)

# Add table caption and styles to DF
stock_info_dataframe.style.pipe(make_pretty).set_caption('Fundamental Indicators').set_table_styles(
    [{'selector': 'th.col_heading', 'props': 'text-align: center'},
     {'selector': 'caption', 'props': [('text-align', 'center'),
                                       ('font-size', '11pt'), ('font-weight', 'bold')]}])
