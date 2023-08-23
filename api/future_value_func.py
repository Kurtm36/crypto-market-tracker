import math
import json
import locale
import requests
from prettytable import PrettyTable

# local set to Ireland 
locale.setlocale(locale.LC_ALL, "en_IE.UTF-8")

local_currency = "EUR"
local_symbol = "€"
# Api Key
API_KEY = "ae55d981-0a3f-4fab-82d8-bfd27701bda3"
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'
GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]

total_market_cap = int(data)["quote"][local_currency]["total_market_cap"]
string_total_market_cap = "{:,}".format(total_market_cap)

# Headers for table found @ https://www.visualcapitalist.com/all-of-the-worlds-money-and-markets-in-one-visualization-2022/
table = PrettyTable(["Name", "Ticker", "% of total global cap", "Current", "11.5T (Gold)", "49.T(Narrow Money)", "95.5T(Stock Markets)"])