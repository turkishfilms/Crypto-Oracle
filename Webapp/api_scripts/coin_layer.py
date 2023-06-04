import sys
import requests
import json
from datetime import date, timedelta

sys.path.append("../")  

from temp.API_KEYS import coinlayer_api_key


def get_coinlayer_prices(coinSymbols):
    symbols = "BTC,ETH,LTC,USDT,ADA"
    url = "http://api.coinlayer.com/live?access_key=" + coinlayer_api_key + "&symbols=" + symbols

    response = requests.get(url)
    data = response.json()
    return data["rates"]
    

def get_coinlayer_prices_yesterday(coinSymbols):
    api_key = coinlayer_api_key
    symbols = "BTC,ETH,LTC,USDT,ADA"
    yesterday = date.today()-timedelta(days=1)
    yesterdizzle = yesterday.isoformat()
    url = f"http://api.coinlayer.com/{yesterdizzle}?access_key=" + api_key + "&symbols=" + symbols + "&expand=1"

    response = requests.get(url)
    data = response.json()
    return data #added rates 
    

if(__name__=="__main__"):
    # coins = get_coinlayer_prices()
    # sys.path.append("../../")  

    coins = get_coinlayer_prices()
    with open("../jsons/CoinLayer_arb.json","w") as j:
        json.dump(coins,j)
    print(coins)
   

