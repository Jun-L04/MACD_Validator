import json

with open('MarketMovement/spy_historical.json', 'r') as file:
    data = json.load(file)

# results array contains all the information
results = data['results']

def count_rates(open_price, close_price):
    return True if close_price > open_price else False

win = 0
loss = 0

for daily_data in results:
    #volume = daily_data['v']  # Volume
    #vwap = daily_data['vw']  # Volume-weighted average price
    open_price = daily_data['o']  # Open price
    close_price = daily_data['c']  # Close price
    #high_price = daily_data['h']  # High price
    #low_price = daily_data['l']  # Low price
    #timestamp = daily_data['t']  # Unix timestamp
    #trades_count = daily_data['n']  # Number of trades
    
    if count_rates(open_price, close_price):
        win += 1
    else:
        loss += 1

win_rate = win / data['queryCount']
loss_rate = loss / data['queryCount']
print(f'Win rate: {win_rate}')
print(f'Loss rate: {loss_rate}')


