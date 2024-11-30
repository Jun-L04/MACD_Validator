from TradingMethods import *
from  datetime import datetime, timedelta
import pandas as pd

# get the past 7 days (yfinance supports 1m interval up to last 7 days)
today = datetime.today()
past_dates = []

for i in range(7):
    past_day = (today - timedelta(days=i)).strftime('%Y-%m-%d')
    past_dates.insert(0, past_day) # dates in reverse order
# get rid of today
# yfinance doesn't have "today" until "tomorrow"
past_dates.pop()

ticker_list = ['spy', 'aapl', 'nvda', 'nio', 'tsla', 'pltr']

# some variables to analyze with
results = {}

for ticker in ticker_list:
    total_pos = 0
    total_neg = 0

    for start_date, end_date in zip(past_dates, past_dates[1:]):
        equity_df = fetch_data(ticker, start_date, end_date) # default 1m interval
        final_profit, _, _ = sim_trade_on_macd(equity_df)
        
        if final_profit > 0:
            total_pos += 1
        else:
            total_neg += 1
    
    positve_rate = total_pos / (total_pos + total_neg)
    negative_rate = total_neg / (total_pos + total_neg)

    results[ticker] = [positve_rate, negative_rate]


# creating table to visualize trading algorithm results using pandas dataframe
table = pd.DataFrame(results, index=['Positive Rate', 'Negative Rate'])

print(table)