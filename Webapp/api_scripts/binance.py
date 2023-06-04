
import requests
import pandas as pd
import json

def get_binance_prices():
    """
    Retrieve current prices for specified symbols from Binance API and return a DataFrame.

    Returns:
        dict: Dict containing the retrieved prices.
    """

    symbols = ["BTCUSD", "ETHUSD", "LTCUSD", "USDTUSD","ADAUSD" ]
    
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

    # return prices
    return {"BTC":float(prices["BTCUSD"]),"LTC":float(prices["LTCUSD"]),"ADA":float(prices["ADAUSD"]),"ETH":float(prices["ETHUSD"]),"USDT":float(prices["USDTUSD"]),}

if(__name__ == "__main__"):
    coins = get_binance_prices()
    print(coins)
    with open("../jsons/Binance_arb.json","w") as ff:
        json.dump(coins,ff)

