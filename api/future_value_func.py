import math
import json
import env
import locale
import requests
from prettytable import PrettyTable

# local set to Ireland 
locale.setlocale(locale.LC_ALL, "en_IE.UTF-8")

local_currency = "EUR"
local_symbol = "€"
# Api Key
API_KEY = os.environ.get("API_KEY")
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'
GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]

encoding = 'utf-8-sig'

total_market_cap = int(data["quote"][local_currency]["total_market_cap"])
string_total_market_cap = "{:,}".format(total_market_cap)

# Table Headers found @ https://www.visualcapitalist.com/all-of-the-worlds-money-and-markets-in-one-visualization-2022/
table = PrettyTable(["Name", "Ticker", "% of total global cap", "Price", "11.5T (Gold)", "49.T(Narrow Money)", "95.5T(Stock Markets)"])

listing_url = BASE_URL + "/v1/cryptocurrency/listings/latest?convert=" + local_currency

request = requests.get(listing_url, headers=headers)
results = request.json()

data = results['data']

for currency in data:
    name = currency["name"]
    ticker = currency["symbol"]
    available_supply = currency["circulating_supply"]

    price = currency['quote'][local_currency]["price"]
    market_cap = currency['quote'][local_currency]["market_cap"]

    percentage_of_global_cap = float(market_cap) / total_market_cap

    # Calculation for future prices(Price is subject to change)
    gold_price = 12747000000000 * percentage_of_global_cap / available_supply
    narrow_money_price = 49900000000000 * percentage_of_global_cap / available_supply
    stock_market_price = 95500000000000 * percentage_of_global_cap / available_supply

    # Formatting
    string_percentage_of_global_cap = str(round(percentage_of_global_cap * 100, 2)) + "%"
    string_price = local_symbol + '{:,}'.format(round(price, 2))
    string_gold_price = local_currency + '{:,}'.format(round(gold_price, 2))
    string_narrow_money = local_currency + "{:,}".format(round(narrow_money_price, 2))
    string_stock_market_money = local_currency + "{:,}".format(round(stock_market_price, 2))

    # Table
    table.add_row([name, ticker, string_percentage_of_global_cap, string_price, string_gold_price, string_narrow_money, string_stock_market_money])

print()
print(table)
print()

