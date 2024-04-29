# BasketBoss

## Authors
Sahil Shah, Vignesh Kumar, & Asad Qureshi

## Description
BasketBoss is a python based portfolio analysis API. Given a basket of stocks and budget for investment purposes, our API will perform various quantitative analysis techniques. Using several scripts you can gain insight on various metrics and even obtain advise on potential positions via signals by incorporating a diverse set of strategies. Functionality can be divided into 2 categories

1. Analysis & Metrics
2. Trading Strategies & Signals

### Analysis & Metrics

**1. Fundamental Analysis:**
Analyze the fundamental factors of each company, such as earnings, revenue growth, debt levels, and valuation metrics like P/E ratios. Understanding the financial health of each company is essential for long-term investment decisions.

	Functionality: 

	- Data Retrieval (DONE): Use yfinance API for Yahoo Finance stock info and Extract key fundamental metrics for analysis
	- Data Analysis (DONE): Use a library like pandas for handling and analyzing the data. Calculate important financial metrics like earnings, revenue growth, debt levels, and valuation ratios. 
	- Presentation (DONE): Present stock basket fundamental analysis (key metrics & ratios along with color gradient ranking for comparison)

	Script:
	fundamental_analysis.py

	Jupyter Notebook:
	fundamental_analysis_notebook.ipynb

3rd Party Libaries:
[yfinance] (https://pypi.org/project/yfinance/)

**2. Historical Performance:**
Examine the historical performance of each stock in the basket. Calculate metrics such as historical returns, volatility, and drawdowns. This can help identify how the stocks have behaved in different market conditions.

	Functionality:

	- Data Analysis (DONE): With the help of the yfinance library, calculate metrics such as historical returns, volatility, and drawdowns
	- Portfolio Optimization (DONE): Given a budget and stock basket, create a Mean-Variance optimized portfolio by creating and Efficient Frontier which is maximizing sharpe ratio using PyPortfolioOpt.

	Script:
	historical_analysis_optimization.py

	Jupyter Notebook:
	historical_analysis_optimization.ipynb

3rd Party Libraries:
[PyPortfolioOpt] (https://pyportfolioopt.readthedocs.io/en/latest/MeanVariance.html)

**3. Correlation and Diversification**
Investigate the correlation between the stocks in the basket. Diversification is crucial for managing risk. If the stocks move in sync, diversification benefits diminish. Analyzing correlation helps in constructing a well-balanced portfolio.

	Functionality:

	- Data gathering & analysis (DONE): Leveraging Polygon API, gather historical close prices and infer daily returns. Create a correlation matrix against the historical returns and plot using Polygon. 

	Script:
	correlation_analysis_optimization.py

	Jupyter Notebook:
	correlation_analysis_optimization.ipynb

3rd Party Libraries:
[Polygon.io](https://polygon.io/blog/finding-correlation-between-stocks)
*** Limited to 5 stock analysis due to free API subscription


### Trading Strategies & Signals

**4. Technical Analysis:**
Examine stock price charts, moving averages, RSI, VWAP, and other technical indicators. This can help identify potential entry and exit points.

	Functionality:

	- Calculate Moving Average (DONE): Using 20-day rolling window on historic close prices. 20-day is a common SMA window for analysis, however multiple combinations should always be explored to obtain an accurate view
	- Presentation (DONE): Plot moving average against historical price chart

References:

- Trading with Moving Average [Moving Average (MA)](https://www.investopedia.com/terms/m/movingaverage.asp#:~:text=The%20Bottom%20Line-,A%20moving%20average%20(MA)%20is%20a%20stock%20indicator%20commonly%20used,moving%20average%20indicates%20a%20downtrend.).


**5. Economic Indicators:**
Analyze macroeconomic indicators and trends. Factors like interest rates, inflation, and geopolitical events can have a significant impact on the overall market and individual stocks.

	Functionality:

	- Gather & Plot historic Federal Funds Rate (interest rates) (DONE)
	- Gather & Plot historic Consumer Price Index (inflation) (DONE)

3rd Party Libraries:
[FRED Economic Data] (https://fred.stlouisfed.org/docs/api/fred/) - The FRED® API is a web service that allows developers to write programs and build applications that retrieve economic data from the FRED® and ALFRED® websites hosted by the Economic Research Division of the Federal Reserve Bank of St. Louis

**6. News and Sentiment Analysis:**
Analyze recent news and sentiment surrounding the stocks. Market sentiment can influence short-term price movements. Tools that analyze news sentiment or social media chatter can provide additional insights (tbd).

	Functionality:

	- Fetch News using VADER API (DONE)
	- Analyze Sentiment using VADER API (DONE)
	- Plot Sentiment Score distribution using matplotlib (DONE)

3rd Party Libraries:
[VADER] (https://pypi.org/project/vaderSentiment/) - VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis api that is specifically attuned to sentiments expressed in social media.

## Future Features
- Risk Management: Assess the overall risk of the portfolio. This involves understanding the risk-return tradeoff and ensuring that the portfolio aligns with your risk tolerance and investment goals.
- Create driver script to invoke API, first with static requests, then streaming requests for a dynamic portfolio
- Host API from Azure or AWS serverless function, Potentially use [Flask](https://flask.palletsprojects.com/en/3.0.x/) for Web App setup.
- Limit API invocation based on limitations of analysis
