import yfinance as yf
import numpy as np


def fetch_data(ticker, start_date, end_date, interval='1m'):
    equity = yf.Ticker(ticker)
    equity_historial = equity.history(
        start=start_date, end=end_date, interval=interval)
    return equity_historial


def get_macd(df):
    ema_12 = df["Open"].ewm(span=12, adjust=False).mean()
    ema_26 = df["Open"].ewm(span=26, adjust=False).mean()

    # macd line
    macd = ema_12 - ema_26
    # signal line
    signal = macd.ewm(span=9, adjust=False).mean()

    return macd, signal


def long(invest_price, current_price):
    shares = invest_price / current_price
    return shares


def sim_trade_on_macd(df):
    """
    df is the dataframe representing the equity's historical data
    """
    idx = 0
    macd, signal = get_macd(df)
    invest_price = 1000.0
    final_profit = 0.0
    shares = 0.0
    strike_price = 0.0
    growth_rate = 0.0
    hold = False  # initially we do not hold the stock

    stats = {'profits': [],
            'buy_time': [],
            'sell_time': []}


    for _, row in df.iterrows():
        # current_price = round(row['Open'], 2)
        current_price = row['Open']
        curr_macd = macd.iloc[idx]
        curr_signal = signal.iloc[idx]

        # macd just cross the signal line
        if curr_macd > curr_signal:
            if not hold:  # do not currently hold a stock
                shares = long(invest_price, current_price)
                strike_price = current_price
                hold = True
                stats['buy_time'].append(current_price)
                stats['sell_time'].append(np.nan)
            else:
                stats['buy_time'].append(np.nan)
                stats['sell_time'].append(np.nan)
        # macd dip below signal line
        elif curr_macd < curr_signal:
            if hold:  # we have stock
                final_profit += shares * (current_price - strike_price)
                shares = 0.0  # sold all shares
                hold = False
                stats['buy_time'].append(np.nan)
                stats['sell_time'].append(current_price)
            else:
                stats['buy_time'].append(np.nan)
                stats['sell_time'].append(np.nan)
        else:
            stats['buy_time'].append(np.nan)
            stats['sell_time'].append(np.nan)
        stats['profits'].append(final_profit)
        # null values, real value represents buy/sell tick

        idx += 1

    growth_rate = final_profit / invest_price * 100

    return final_profit, growth_rate, stats
