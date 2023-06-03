# %%
import requests
import pandas as pd

# %%
def get_coingecko_prices():
    """
    Retrieve coin data from the CoinGecko API and return a DataFrame.
    """
    # Set up the API endpoint
    url = 'https://api.coingecko.com/api/v3/'

    # Make a GET request to retrieve the data
    # print("idkHomies")
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
        # print(data)
        print("coingecko")
        #create a lists to hold
        coin_data = []
        for coin in data:
            coin_data.append({"Symbol": coin['symbol'], "Price": coin['current_price']})
            
        # todays_price = pd.DataFrame(coin_data)
        # todays_price["Price"] = pd.to_numeric(todays_price["Price"])
        # todays_price = todays_price.sort_values(by='Price', ascending=False)
        # todays_price["Price"] = todays_price["Price"].map('${:,.2f}'.format)
        
        rename_symbols = {'btc': 'BTCUSD',
                          'eth' : 'ETHUSD',
                          'ltc' : 'LTCUSD',
                          'usdt': 'USDTUSD',
                          'ada' : 'ADAUSD'}
        # todays_price['Symbol'] = todays_price['Symbol'].replace(rename_symbols)
            
        return coin_data
    else :
        print(response.status_code)
            

# %%
# coin_data = get_coinGecko_coin_data()
# coin_data

if(__name__ == "__main__"):
    get_coingecko_prices()


