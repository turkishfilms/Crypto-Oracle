
import requests
import pandas as pd
import json

def get_binance_prices(coin_symbols):
    """
    Retrieve current prices for specified symbols from Binance API and return a DataFrame.

    Returns:
        dict: Dict containing the retrieved prices.
    """
    
    symbols_str = ','.join([f'"{symbol}USD"' for symbol in coin_symbols])
    req = 'https://api.binance.us/api/v3/ticker/price?symbols=[' + symbols_str + ']'
    data = requests.get(req).json()
    return  {coin['symbol'][:-3]: float(coin['price']) for coin in data}

if(__name__ == "__main__"):
    coins = get_binance_prices([])
    print(coins)
    with open("../jsons/Binance_arb.json","w") as ff:
        json.dump(coins,ff)

