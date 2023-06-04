import requests
import pandas as pd
import json

def get_coingecko_prices(coin_symbols):
    """
    Retrieve coin data from the CoinGecko API and return a DataFrame.
    """
    with open("list.json","r") as conv:
        convert_to_id = json.load(conv)

    ids = ','.join([convert_to_id[coin.lower()] for coin in coin_symbols])

    url = 'https://api.coingecko.com/api/v3/'
    response = requests.get(url + 'coins/markets', params={
        'vs_currency': 'usd',
        'ids': ids,
        'order': 'market_cap_desc',
        'sparkline': False
    })
   
    if response.status_code == 200:
        data = response.json()
        return {[coin['symbol'].upper()] : coin['current_price'] for coin in data}
    else :
        print(response.status_code)
            
if(__name__ == "__main__"):
    coins = get_coingecko_prices()
    print(coins)
    with open("../jsons/CoinGecko_arb.json","w") as j:
        json.dump(coins,j)


