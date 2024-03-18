# BasketBoss

## Authors
Sahil Shah, Vignesh Kumar, & Asad Qureshi

## Description
BasketBoss is a python based portfolio analysis API. Given a basket of stocks for investment purposes, our API will perform quantitative analysis to gain insight on various metrics and ultimately advise on potential positions via signals by incorporating a diverse set of strategies. Functionality can be divided into 2 categories

1. Analysis & Metrics
2. Trading Strategies & Signals

### Analysis & Metrics

**1. Fundamental Analysis:**
Analyze the fundamental factors of each company, such as earnings, revenue growth, debt levels, and valuation metrics like P/E ratios. Understanding the financial health of each company is essential for long-term investment decisions.

	Functionality: 

	- Data Retrieval (DONE): Use yfinance API for Yahoo Finance stock info and Extract key fundamental metrics for analysis
	- Data Analysis (DONE): Use a library like pandas for handling and analyzing the data. Calculate important financial metrics like earnings, revenue growth, debt levels, and valuation ratios. 
	- Presentation (DONE): Present stock basket fundamental analysis (key metrics & ratios along with color gradient ranking for comparison)

	Scripts:

	fundamental_analysis.py
	fundamental_analysis_notebook.ipynb


**2. Historical Performance:**
Examine the historical performance of each stock in the basket. Calculate metrics such as historical returns, volatility, and drawdowns. This can help identify how the stocks have behaved in different market conditions.

	TODO:

	- Data Analysis: With the help of the yfinance library, calculate metrics such as historical returns, volatility, and drawdowns

**3. Correlation and Diversification**
Investigate the correlation between the stocks in the basket. Diversification is crucial for managing risk. If the stocks move in sync, diversification benefits diminish. Analyzing correlation helps in constructing a well-balanced portfolio.

	TODO:

	- Explore ways to determine stock correlation - [Polygon.io](https://polygon.io/blog/finding-correlation-between-stocks)


### Trading Strategies & Signals

**4. Technical Analysis:**
Examine stock price charts, moving averages, RSI, VWAP, and other technical indicators. This can help identify potential entry and exit points.

TODO:

- Trading with Moving Average [Moving Average (MA)](https://www.investopedia.com/terms/m/movingaverage.asp#:~:text=The%20Bottom%20Line-,A%20moving%20average%20(MA)%20is%20a%20stock%20indicator%20commonly%20used,moving%20average%20indicates%20a%20downtrend.).
- Trading with RSI [Relative Strength Index (RSI)](https://www.investopedia.com/terms/r/rsi.asp).
- Trading With VWAP and MVWAP [TWAP & VWAP](https://www.investopedia.com/articles/trading/11/trading-with-vwap-mvwap.asp#:~:text=General%20Strategies,-When%20a%20security&text=If%20the%20price%20is%20above,not%20be%20by%20day's%20end.).

**5. Economic Indicators:**
Analyze macroeconomic indicators and trends. Factors like interest rates, inflation, and geopolitical events can have a significant impact on the overall market and individual stocks.

**6. News and Sentiment Analysis:**
Analyze recent news and sentiment surrounding the stocks. Market sentiment can influence short-term price movements. Tools that analyze news sentiment or social media chatter can provide additional insights (tbd).

	TODO:

	- Find open source news sentiment api

### Risk Management
7. Assess the overall risk of the portfolio. This involves understanding the risk-return tradeoff and ensuring that the portfolio aligns with your risk tolerance and investment goals.



## "Nice to Have"

- Create driver script to invoke API, first with static requests, then streaming requests for a dynamic portfolio
- Host API from Azure or AWS serverless function, Potentially use [Flask](https://flask.palletsprojects.com/en/3.0.x/) for Web App setup.
- Limit API invocation based on limitations of analysis
