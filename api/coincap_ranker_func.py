import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'EUR'
local_symbol = '€'

API_KEY = "ae55d981-0a3f-4fab-82d8-bfd27701bda3"
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'

print()
print("CoinMarketCap Explorer Menu")
print()
print("[1]- Top 100 sorted by market cap")
print("[2]- Top 100 sorted by 24hr percent change")
print("[3]- Top 100 sorted by 24hr trading volume")
print("[0]- Exit")

choice = input("What information would you like to view? (1-3)")

sort = ""

if choice == "1":
    sort = "market_cap"
elif choice == "2":
    sort = "percent_change_24h"
elif choice == "3":
    sort = "volume_24h"
elif choice == "0":
    exit(0)
else:
    print("Invalid choice")
    exit(1)

quote_url = BASE_URL + "/v1/cryptocurrency/listings/latest?convert=" + local_currency + "&sort=" + sort

request = requests.get(quote_url, headers=headers)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))