#!/usr/bin/env python
# coding: utf-8

import json 
import threading
import time

from joblib import load
import pandas as pd
from itertools import combinations

from flask import Flask, render_template, jsonify
from flask_cors import CORS

from api_scripts.livecoin import get_livecoin_prices
from api_scripts.binance import get_binance_prices 
from api_scripts.coin_gecko import get_coingecko_prices 
from api_scripts.coin_layer import get_coinlayer_prices, get_coinlayer_prices_yesterday 


coins = ["BTC","LTC","ETH","ADA","USDT"]
markets = {
        "CoinGecko" : get_coingecko_prices,
        "CoinLayer" : get_coinlayer_prices,
        "Binance" : get_binance_prices,
        "Livecoin" : get_livecoin_prices
    }

main_data = {}
models={}

def opportunity(seller_market,buy_price,buyer_market,sell_price,coin):
    return{"coin":coin,
    "sellerMarket":seller_market,
    "buyPrice":buy_price,
    "buyerMarket":buyer_market,
    "sellPrice":sell_price }
    

def compare(m1,m2,coin): #add number formatting and threshold
    m2price = main_data["data"][m2][coin]
    m1price = main_data["data"][m1][coin]

    if(m1price == m2price):
        return False
    
    if(m1price > m2price): 
        return opportunity(m2,m2price,m1,m1price,coin)
    else:
        return opportunity(m1,m1price,m2,m2price,coin)


def get_coin_prices(stale, coins,markets):
    prices_by_market = {}
    
    if stale == False:
        for market in markets:
            prices_by_market[market] = markets[market](coins) 
    else:
        with open("main_data.json","r") as cl:
            main = json.load(cl)["data"]
        for market in markets:
            prices_by_market[market] = main[market]

    return prices_by_market
    

def get_arbitrage_opportunities():
    opportunities = []
    for coin in coins:
        comps = []
        for market_pair in combinations(markets, 2):
            comps.append(compare(market_pair[0],market_pair[1],coin))
        for comp in comps:
            if comp != False:
                opportunities.append(comp)
    return opportunities


def get_yesterdays_data(stale):
    if stale == True:
        with open("main_data.json","r") as cl:
            yesterdata = json.load(cl)["yester"]
    else:
        yesterdata = get_coinlayer_prices_yesterday(coins)
    return yesterdata


def retrieveModels():
    mls = {}
    for coin in coins:
        mls[coin] = load(f'ml/regressor_{coin}.joblib') 
    return mls


def model_preds():
    final_pred = {}
    coin_data = main_data["yester"]
    for coin in coins:
        final_pred[coin] = list(models[coin].predict(pd.DataFrame(coin_data[coin])))[0]
    return final_pred


def get_data_on_delay():
    while True:
        staleness = False
        main_data["data"] = get_coin_prices(staleness,coins,markets)
        main_data["ops"] = get_arbitrage_opportunities()
        main_data["yester"] = get_yesterdays_data(staleness)
        main_data["pred_data"] = model_preds()
        with open("main_data.json","w") as mj:
            json.dump(main_data,mj)
        time.sleep(120) #four hours


models = retrieveModels()   

main_data["data"] = get_coin_prices(True,coins,markets)
main_data["ops"] = get_arbitrage_opportunities()
main_data["yester"] = get_yesterdays_data(True)
main_data["pred_data"] = model_preds()


app = Flask(__name__)

CORS(app,resources={r"/*": {"origins": ["https://turkishfilms.github.io"]}})


@app.route('/')
def home():
   return render_template('index.html',data=main_data["ops"])

@app.route('/learn')
def learning():
    return render_template('learn.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html', data = json.dumps({"pred_data": main_data["pred_data"], "current_data": main_data["data"], "yesterday_data": main_data["yester"]}))

if(__name__ == "__main__"):
    app_thread = threading.Thread(target=get_data_on_delay)
    app_thread.start()
    app.run()

