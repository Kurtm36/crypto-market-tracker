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

symbol = input("Enter the ticker symbol of the cryptocurrency(CAP SENSITIVE I.E BTC , XRP , ETH) : ")

GLOBAL_URL = BASE_URL + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + "&symbol=" + symbol

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]
currency = data[symbol]
name = currency["name"]

#Pulling data varibles
price = currency["quote"][local_currency]["price"]
percent_change_24hr = currency["quote"][local_currency]["percent_change_24h"]
percent_change_7day = currency["quote"][local_currency]["percent_change_7d"]
percent_change_30day = currency["quote"][local_currency]["percent_change_30d"]
market_cap = currency["quote"][local_currency]["market_cap"]

#Rounding data
price = round(price , 2)
percent_change_24hr = round(percent_change_24hr, 2)
percent_change_7day = round(percent_change_7day, 2)
percent_change_30day = round(percent_change_30day, 2)
market_cap = round(market_cap, 2)

#Formatting data
string_price = local_symbol + "{:,}".format(price)
string_percent_change_24hr = local_currency + "{:,}".format(percent_change_24hr)
string_percent_change_7day = local_currency + "{:,}".format(percent_change_7day)
string_percent_change_30day = local_currency + "{:,}".format(percent_change_30day)
string_market_cap = local_currency + "{:,}".format(market_cap)

#Printing the data
print(name + " (" + symbol +")")
print("Price : " + string_price)
print("24hr Change : " + string_percent_change_24hr)
print("7 Day Change : " + string_percent_change_7day)
print("3 Day Change : " + string_percent_change_30day)
print("Market Cap : " + string_market_cap + "\n")