# %%
# import config
import requests
import pandas as pd
import json

# %%
def get_binance_prices(symbols):
    """
    Retrieve current prices for specified symbols from Binance API and return a DataFrame.

    Parameters:
        symbols (list): List of symbols to retrieve prices for.

    Returns:
        pandas.DataFrame: DataFrame containing the retrieved prices.
    """
    # Make a GET request to retrieve the data from Binance API
    current_prices = requests.get('https://api.binance.us/api/v3/ticker/price')
    data = current_prices.json()

    # Collect the prices for the specified symbols
    prices = {}
    for item in data:
        symbol = item['symbol']
        price = item['price']
        if symbol in symbols:
            prices[symbol] = price

   # Create a DataFrame from the collected prices
    todays_prices_binance = pd.DataFrame(prices.items(), columns=["Symbol", "Price"])

    return prices

# Specify the symbols you want to retrieve prices for
# symbols = ["BTCUSD", "ETHUSD", "LTCUSD", "ADAUSD", "USDTUSD"]

# Call the function to retrieve the prices and store in a variable
# prices_binance = get_binance_prices(["BTCUSD", "ETHUSD", "LTCUSD", "USDTUSD","ADAUSD" ])
# with open("barb.json","w")as ff:
#     json.dump(prices_binance,ff)
# prices_binance["Price"] = pd.to_numeric(prices_binance["Price"])
# prices_binance["Price"] = prices_binance["Price"].apply('${:,.2f}'.format)

# # Print the retrieved prices
# prices_binance


if(__name__ == "__main__"):
    prices_binance = get_binance_prices(["BTCUSD", "ETHUSD", "LTCUSD", "USDTUSD","ADAUSD" ])
    with open("barb.json","w")as ff:
        json.dump(prices_binance,ff)

