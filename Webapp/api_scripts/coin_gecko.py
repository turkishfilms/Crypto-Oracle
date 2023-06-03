import requests
import pandas as pd
import json

def get_coingecko_prices():
    """
    Retrieve coin data from the CoinGecko API and return a DataFrame.
    """
    # Set up the API endpoint
    url = 'https://api.coingecko.com/api/v3/'

    # Make a GET request to retrieve the data
    response = requests.get(url + 'coins/markets', params={
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,tether,litecoin,cardano',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    })

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Retrieve the response data
        data = response.json()
        # Create a lists to hold
        coin_data = []
        for coin in data:
            coin_data.append({"Symbol": coin['symbol'], "Price": coin['current_price']})
        return coin_data
    else :
        print(response.status_code)
            
if(__name__ == "__main__"):
    coins = get_coingecko_prices()
    print(coins)
    with open("../jsons/cgarb.json","w") as j:
        json.dump(coins,j)


