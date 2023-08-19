import requests    
import json

local_currency = 'EUR'
local_symbol = '€'

"""
API Key varible. Generated @ https://pro.coinmarketcap.com/account . Login Creds will be in README if required.
"""
API_KEY = "ae55d981-0a3f-4fab-82d8-bfd27701bda3"
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'
GLOBAL_URL = BASE_URL + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]

for currency in data : 
    name = currency["name"]
    symbol = currency["symbol"]

    price = currency["quote"][local_currency]["price"]
    percent_change_24hr = currency["quote"][local_currency]["percent_change_24h"]
    percent_change_7day = currency["quote"][local_currency]["percent_change_7d"]
    percent_change_30day = currency["quote"][local_currency]["percent_change_30d"]
    market_cap = currency["quote"][local_currency]["market_cap"]
    
    
