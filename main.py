# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd

# Bybit API URL for historical kline data
url = 'https://api.bybit.com/v2/public/kline/list'

# Define the parameters for the API request
symbol = 'BTCUSD'  # Symbol for BTC/USD pair
interval = '1'     # Time interval (1 minute)
start_time = '1609459200'  # Start time in Unix timestamp format (e.g., '1609459200' for Jan 1, 2021)
end_time = '1622505600'    # End time in Unix timestamp format (e.g., '1622505600' for May 31, 2021)

params = {
    'symbol': symbol,
    'interval': interval,
    'from': start_time,
    'to': end_time
}

# Send GET request to the API
response = requests.get(url, params=params)
data = response.json()

# Convert the response data to a Pandas DataFrame
df = pd.DataFrame(data['result'])

# Convert timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['open_time'], unit='s')

# Print the collected data
print(df)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



