import requests    
import json
import os

local_currency = 'EUR'
local_symbol = '€'

API_KEY = "ae55d981-0a3f-4fab-82d8-bfd27701bda3"
headers = {"X-CMC_PRO_API_KEY": API_KEY}

# Global Market data Function
def global_market_data(local_currency, local_symbol):
    
    BASE_URL = 'https://pro-api.coinmarketcap.com'
    GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + local_currency

    request = requests.get(GLOBAL_URL, headers=headers)
    results = request.json()

    #print(json.dumps(results, sort_keys=True, indent=4))
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
    Ethereum Dominance
    """
    eth_dominance = data["eth_dominance"]
    eth_dominance = round(eth_dominance, 2)

    print("Ethereum makes up " + str(eth_dominance) + "%" + " of the global market cap")
execute_global_data = True

# Global Listings Of Cryptos Function
def coincap_coin_listings(local_currency, local_symbol):
    BASE_URL = 'https://pro-api.coinmarketcap.com'
    GLOBAL_URL = BASE_URL + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

    request = requests.get(GLOBAL_URL, headers=headers)
    results = request.json()

    #print(json.dumps(results, sort_keys=True, indent=4))
    data = results["data"]

    for currency in data : 
        name = currency["name"]
        symbol = currency["symbol"]
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
execute_coincap_listings = True

# Clear text for function for terminal 
def clear_text_terminal():
    os.system("cls" if os.name =="nt" else "clear")

# Terminal Menu
def display_Menu():
    print("Kurts Cypto Data Center")
    print("Select 1 for Global Market Data")
    print("Select 2 for Global listings Data ")
    print("Select 3 for Global Market Data")
    print("Select 4 for Global Market Data")
    print("Select 5 for Global Market Data")
    print("Select 0 to Exit")

while True:
    clear_text_terminal()   
    display_Menu()
    
    keyboardValue = input()
    user_input = int(keyboardValue)
    
    if user_input == 1 and execute_global_data:
        clear_text_terminal()   
        global_market_data(local_currency, local_symbol)
        execute_global_data = False
        input("Press [Enter] to return to Menu")
        execute_global_data = True
    elif user_input == 2 and execute_coincap_listings:
        clear_text_terminal()
        coincap_coin_listings(local_currency, local_symbol) 
        execute_coincap_listings = False  
        input("Press [Enter] to return to Menu")
        execute_coincap_listings = True
    elif user_input == 3:
        clear_text_terminal()   
        print("you have selected [3]")
        input("Press [Enter] to return to Menu")
    elif user_input == 4:
        clear_text_terminal()   
        print("you have selected [4]")
        input("Press [Enter] to return to Menu")
    elif user_input == 5:
        clear_text_terminal()   
        print("You have selected [5]")
        input("Press [Enter] to return to Menu")
    elif user_input == 0:
        clear_text_terminal()   
        print("Exiting the program...")
        break
    else:
        clear_text_terminal()   
        print("Invalid option. Please select a valid option.")
        input("Press [Enter] to return to Menu")
