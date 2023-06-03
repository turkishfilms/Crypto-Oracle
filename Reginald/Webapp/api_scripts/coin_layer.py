# %%
# Dependencies
import requests
import json
# from config import api_key
from pprint import pprint

    # %%
import pandas as pd
def get_coinlayer_prices():
    api_key = "9d86b497a3fa7cade4d489127a4c9d3b"
    symbols = "BTC,ETH,LTC,USDT,ADA"
    url = "http://api.coinlayer.com/live?access_key=" + api_key + "&symbols=" + symbols

    response = requests.get(url)
    data = response.json()
    with open("clarb.json","w") as j:
        json.dump(data,j)
    return json.dumps(data)
    # Access the cryptocurrency values
    btc_value = data['rates']['BTC']
    eth_value = data['rates']['ETH']
    ltc_value = data['rates']['LTC']
    usdt_value = data['rates']['USDT']
    ada_value = data['rates']['ADA']

    # Format the values with a dollar sign and rounding
    btc_value_formatted = "${:.2f}".format(btc_value)
    eth_value_formatted = "${:.2f}".format(eth_value)
    ltc_value_formatted = "${:.2f}".format(ltc_value)
    usdt_value_formatted = "${:.2f}".format(usdt_value)
    ada_value_formatted = "${:.2f}".format(ada_value)

    coin_values = [btc_value_formatted,eth_value_formatted,ltc_value_formatted,usdt_value_formatted,ada_value_formatted]

    # Define the cryptocurrency names
    cryptocurrency_names = {
        'BTC': 'Bitcoin',
        'ETH': 'Ethereum',
        'LTC': 'Litecoin',
        'USDT': 'Tether',
        'ADA': 'Cardano'
    }
    coin_names = ['BTC','ETH','LTC','USDT','ADA']
    # Create a DataFrame
    data = {
        'Cryptocurrency': [cryptocurrency_names['BTC'], cryptocurrency_names['ETH'], cryptocurrency_names['LTC'],
                           cryptocurrency_names['USDT'], cryptocurrency_names['ADA']],
        'Abbreviation': ['BTC', 'ETH', 'LTC', 'USDT', 'ADA'],
        'Value (USD)': [btc_value_formatted, eth_value_formatted, ltc_value_formatted, usdt_value_formatted, ada_value_formatted]
    }

    coin_data = []

    for i,name in coin_names:
        coin_data.append({"Symbol": name,"value": coin_values[i]})

    df = pd.DataFrame(data)
    # Display the DataFrame
    print(df)
    # return zip(coin_names,coin_values)
    return coin_data

if(__name__=="__main__"):
    coins = get_coinlayer_prices()
    print(coins)
    # with open("clarb.json","r") as j:
    #     json.dump(coins,j)
