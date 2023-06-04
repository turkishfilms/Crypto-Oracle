import sys
import requests
import json
from datetime import datetime, date, timedelta

sys.path.append("../")  

from temp.API_KEYS import coinlayer_api_key2


def get_coinlayer_prices(coinSymbols):
    symbols = "BTC,ETH,LTC,USDT,ADA"
    symbols2 = coinSymbols
    url = "http://api.coinlayer.com/live?access_key=" + coinlayer_api_key2 + "&symbols=" + symbols

    response = requests.get(url)
    data = response.json()
    return data["rates"]
    

def get_coinlayer_prices_yesterday(coinSymbols):
    api_key = coinlayer_api_key2
    symbols = "BTC,ETH,LTC,USDT,ADA"
    symbols2 = coinSymbols
    yesterday = date.today()-timedelta(days=1)
    yesterdizzle = yesterday.isoformat()
    url = f"http://api.coinlayer.com/{yesterdizzle}?access_key=" + api_key + "&symbols=" + symbols + "&expand=1"

    response = requests.get(url)

    yesterdata = response.json()
    yestercoins = yesterdata["rates"]

    formatted_data={}
    for coin in yestercoins:
        formatted_data[coin] = {
        "Open":[yestercoins[coin]["rate"]],
        "High":[yestercoins[coin]["high"]],
        "Low":[yestercoins[coin]["low"]],
        "Close":[yestercoins[coin]["rate"]],
        "Adj Close":[yestercoins[coin]["rate"]],
        "Volume":[yestercoins[coin]["vol"]],
        "year":[yesterday.year],
        "month":[yesterday.month],
        "day":[yesterday.day],}
    return formatted_data 
    

if(__name__=="__main__"):
    # coins = get_coinlayer_prices()
    # sys.path.append("../../")  

    coins = get_coinlayer_prices_yesterday([])
    with open("jsons/CoinLayer_Yesterday_arb.json","w") as j:
        json.dump(coins,j)
    print(coins)
   

