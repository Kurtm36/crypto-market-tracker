import json
import requests
import env
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'EUR'
local_symbol = '€'

API_KEY = os.environ.get("API_KEY")
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'

# Menu for Ranking Function

print()
print("CoinMarketCap Explorer Menu")
print()
print("[1]- Top 100 Sorted By Market cap")
print("[2]- Top 100 Sorted By 24hr Trading Volume ")
print("[3]- Top 100 Sorted By 24hr Percent Change")
print("[4]- Top 100 Sorted By 7 day Change")
print()
print("[0]- Exit")

choice = input("What information would you like to view? (1-3 or 0 to exit) :  ")

if choice == "1":
    sort = "market_cap"
elif choice == "2":
    sort = "volume_24h"
elif choice == "3":
    sort = "percent_change_24h"
elif choice == "4":
    sort = "percent_change_7d"   
else:
    print("Invalid choice. Please select a valid option.")
    input("Press [Enter] to return to Main-Menu")


quote_url = BASE_URL + "/v1/cryptocurrency/listings/latest?convert=" + local_currency + "&sort=" + sort

request = requests.get(quote_url, headers=headers)
results = request.json()

# Api Data
data = results["data"]

#Table Varible
table = PrettyTable(["Asset", "Price", "Market_Cap", "Volume", "1hr", "24hr" ,"7d", "30d"])

print()

for currency in data:
    name = currency["name"]
    symbol = currency["symbol"]
    # Data for Table
    quote = currency["quote"][local_currency]
    market_cap = quote["market_cap"]

    percent_change_1hr = quote["percent_change_1h"]
    percent_change_24hr = quote["percent_change_24h"]
    percent_change_7d = quote["percent_change_7d"]
    percent_change_30d = quote["percent_change_30d"]

    price = quote["price"]
    volume = quote["volume_24h"]
    # Formatting data with Color Indicators    
    if percent_change_1hr is not None:
        percent_change_1hr = round(percent_change_1hr, 2)
        if percent_change_1hr > 0:
            percent_change_1hr = Back.GREEN + str(percent_change_1hr) + "%" + Style.RESET_ALL
        else:
            percent_change_1hr = Back.RED + str(percent_change_1hr) + "%" + Style.RESET_ALL    
        
    if percent_change_24hr is not None:
        percent_change_24hr = round(percent_change_24hr, 2)
        if percent_change_24hr > 0:
            percent_change_24hr = Back.GREEN + str(percent_change_24hr) + "%" + Style.RESET_ALL
        else:
            percent_change_24hr = Back.RED + str(percent_change_24hr) + "%" + Style.RESET_ALL

    if percent_change_7d is not None:
        percent_change_7d = round(percent_change_7d, 2)
        if percent_change_7d > 0:
            percent_change_7d = Back.GREEN + str(percent_change_7d) + "%" + Style.RESET_ALL
        else:
            percent_change_7d = Back.RED + str(percent_change_7d) + "%" + Style.RESET_ALL

    if percent_change_30d is not None:
        percent_change_30d = round(percent_change_30d, 2)
        if percent_change_30d > 0:
            percent_change_30d = Back.GREEN + str(percent_change_30d) + "%" + Style.RESET_ALL
        else:
            percent_change_30d = Back.RED + str(percent_change_30d) + "%" + Style.RESET_ALL            

    if volume is not None:
        volume_string = "{:,}".format(round(volume, 2))

    if market_cap is not None:
        market_cap_string = "{:,}".format(round(market_cap, 2))

    price_string = "{:,}".format(round(price, 2)) 
    # Table formatting 
    table.add_row([name + " (" + symbol + ')',
                   local_symbol + price_string,
                   local_symbol + market_cap_string,
                   local_symbol + volume_string,
                   str(percent_change_1hr),
                   str(percent_change_24hr),
                   str(percent_change_7d),
                   str(percent_change_30d),]) 


print()
print(table)
print()           