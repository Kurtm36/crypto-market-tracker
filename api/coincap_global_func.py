import requests    
import json
import os 
local_currency = 'EUR'
local_symbol = '€'

"""
API Key varible. Generated @ https://pro.coinmarketcap.com/account . Login Creds will be in README if required.
"""
API_KEY = os.environ.get("API_KEY")
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'
GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]


"""
Total Market Cap
"""
total_market_cap = data["quote"][local_currency]["total_market_cap"]
total_market_cap = round(total_market_cap, 2)
total_market_cap_string = local_symbol + "{:,}".format(total_market_cap)

print("The global market cap for all cryptocurrencies is : " + total_market_cap_string)

"""
Total Market Volume 24hr
"""
total_volume_24hr = data["quote"][local_currency]["total_volume_24h"]
total_volume_24hr = round(total_volume_24hr, 2)
total_volume_24hr_string = local_symbol + "{:,}".format(total_volume_24hr)

print("The total global trading volume is : " + total_volume_24hr_string)

"""
Bitcoin Dominance Float (BTC Market cap)
"""
btc_dominance = data["btc_dominance"]
btc_dominance = round(btc_dominance, 2)

print("Bitcoin makes up " + str(btc_dominance) + "%" + " of the global market cap")

"""
Etherium Dominance
"""
eth_dominance = data["eth_dominance"]
eth_dominance = round(eth_dominance, 2)

print("Etherium makes up " + str(eth_dominance) + "%" + " of the global market cap")