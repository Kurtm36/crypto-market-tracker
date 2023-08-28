import os
import requests
from prettytable import PrettyTable
from colorama import Back, Style

if os.path.exists('env.py'):
    import env

local_currency = 'EUR'
local_symbol = '€'

API_KEY = os.environ.get("API_KEY")
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'

# Global Market data Function


def global_market_data(local_currency, local_symbol):
    """
    Docstring goes here
    """

    local_currency = 'EUR'
    local_symbol = '€'

    # BASE_URL = 'https://pro-api.coinmarketcap.com'
    GLOBAL_URL = (
        BASE_URL +
        '/v1/global-metrics/quotes/latest?convert=' +
        local_currency
    )
    try:
        request = requests.get(GLOBAL_URL, headers=headers, timeout=15)
        results = request.json()

        # print(json.dumps(results, sort_keys=True, indent=4))
        data = results["data"]

        # Total Market Cap
        total_market_cap = data["quote"][local_currency]["total_market_cap"]
        total_market_cap = round(total_market_cap, 2)
        total_market_cap_string = local_symbol + "{:,}".format(
            total_market_cap
        )

        print(
            "The global market cap for all cryptocurrencies is : " +
            total_market_cap_string)

        # Total Market Volume 24hr
        total_volume_24hr = data["quote"][local_currency]["total_volume_24h"]
        total_volume_24hr = round(total_volume_24hr, 2)
        total_volume_24hr_string = local_symbol + \
            "{:,}".format(total_volume_24hr)

        print(
            "The total global trading volume is : " +
            total_volume_24hr_string
        )

        # Bitcoin Dominance Float (BTC Market cap)
        btc_dominance = data["btc_dominance"]
        btc_dominance = round(btc_dominance, 2)

        print(
            "Bitcoin makes up " + str(btc_dominance) + "%" +
            " of the global market cap")

        # Ethereum Dominance
        eth_dominance = data["eth_dominance"]
        eth_dominance = round(eth_dominance, 2)

        print(
            "Ethereum makes up " + str(eth_dominance) + "%" +
            " of the global market cap")
    except KeyError as key_ex:
        print("Error, please try again")


execute_global_data = True

# Global Listings Of Cryptocurrencies Function


def coincap_coin_listings(local_currency, local_symbol):
    # BASE_URL = 'https://pro-api.coinmarketcap.com'
    GLOBAL_URL = (
        BASE_URL +
        '/v1/cryptocurrency/listings/latest?convert=' +
        local_currency
    )
    try:
        request = requests.get(GLOBAL_URL, headers=headers, timeout=15)
        results = request.json()

        # print(json.dumps(results, sort_keys=True, indent=4))
        data = results["data"]

        for currency in data:
            name = currency["name"]
            symbol = currency["symbol"]
            # Pulling data varibles
            price = currency["quote"][local_currency]["price"]
            percent_change_24hr = currency["quote"][local_currency][
                "percent_change_24h"]
            percent_change_7day = currency["quote"][local_currency][
                "percent_change_7d"]
            percent_change_30day = currency["quote"][local_currency][
                "percent_change_30d"]
            market_cap = currency["quote"][local_currency]["market_cap"]
            # Rounding data
            price = round(price, 2)
            percent_change_24hr = round(percent_change_24hr, 2)
            percent_change_7day = round(percent_change_7day, 2)
            percent_change_30day = round(percent_change_30day, 2)
            market_cap = round(market_cap, 2)
            # Formatting data
            string_price = local_symbol + "{:,}".format(price)
            string_percent_change_24hr = "{:,}%".format(percent_change_24hr)
            string_percent_change_7day = "{:,}%".format(percent_change_7day)
            string_percent_change_30day = "{:,}%".format(percent_change_30day)
            string_market_cap = local_currency + "{:,}".format(market_cap)
            # Printing the data
            print(name + " (" + symbol + ")")
            print("Price : " + string_price)
            print("24hr Change : " + string_percent_change_24hr)
            print("7 Day Change : " + string_percent_change_7day)
            print("3 Day Change : " + string_percent_change_30day)
            print("Market Cap : " + string_market_cap + "\n")
    except KeyError as key_ex:
        print("Error, please try again")


execute_coincap_listings = True

# Cypto Price Quotes Function(Enter ticker symbol (CAPS ONLY))


def coincap_quotes():

    # BASE_URL = 'https://pro-api.coinmarketcap.com'

    symbol = input(
        "Enter the ticker symbol of the cryptocurrency" +
        "(CAP SENSITIVE I.E BTC , XRP , ETH) : "
    ).upper()

    GLOBAL_URL = (
        BASE_URL +
        '/v1/cryptocurrency/quotes/latest?convert=' +
        local_currency +
        "&symbol=" +
        symbol
    )
    try:
        request = requests.get(GLOBAL_URL, headers=headers, timeout=15)
        results = request.json()

        # Basic coin infomation
        data = results["data"]
        currency = data[symbol]
        name = currency["name"]

        # Pulling data varibles
        price = currency["quote"][local_currency]["price"]
        percent_change_24hr = currency["quote"][local_currency][
            "percent_change_24h"]
        percent_change_7day = currency["quote"][local_currency][
            "percent_change_7d"]
        percent_change_30day = currency["quote"][local_currency][
            "percent_change_30d"]
        market_cap = currency["quote"][local_currency]["market_cap"]

        # Rounding data
        price = round(price, 2)
        percent_change_24hr = round(percent_change_24hr, 2)
        percent_change_7day = round(percent_change_7day, 2)
        percent_change_30day = round(percent_change_30day, 2)
        market_cap = round(market_cap, 2)

        # Formatting data
        string_price = local_symbol + "{:,}".format(price)
        string_percent_change_24hr = "{:,}%".format(percent_change_24hr)
        string_percent_change_7day = "{:,}%".format(percent_change_7day)
        string_percent_change_30day = "{:,}%".format(percent_change_30day)
        string_market_cap = local_currency + "{:,}".format(market_cap)

        # Printing the data
        print(name + " (" + symbol + ")")
        print("Price : " + string_price)
        print("24hr Change : " + string_percent_change_24hr)
        print("7 Day Change : " + string_percent_change_7day)
        print("3 Day Change : " + string_percent_change_30day)
        print("Market Cap : " + string_market_cap + "\n")
    except KeyError as key_ex:
        print("Error, please try again")
        coincap_quotes()


execute_coincap_quotes = True

# Top 100 Crypto Performance Ranker


def coincap_ranker():

    local_currency = 'EUR'
    local_symbol = '€'

    # BASE_URL = 'https://pro-api.coinmarketcap.com'

    # Menu for Ranking Function

    print()
    print("CoinMarketCap Explorer Menu")
    print()
    print("[1]- Top 100 Sorted By Market cap")
    print("[2]- Top 100 Sorted By 24hr Trading Volume ")
    print("[3]- Top 100 Sorted By 7 day Change")
    print()
    print("[0]- Exit")

    choice = input("What information would you like to view? (1-3 or 0 to exit): ")

    if choice == "1":
        sort = "market_cap"
    elif choice == "2":
        sort = "volume_24h"
    elif choice == "3":
        sort = "percent_change_7d"
    else:
        print("Invalid choice. Please select a valid option.")
        return  # Exit the function if the choice is invalid

    quote_url = (
        BASE_URL +
        "/v1/cryptocurrency/listings/latest?convert=" +
        local_currency +
        "&sort=" +
        sort
    )
    try:
        request = requests.get(quote_url, headers=headers)
        results = request.json()

        # Api Data
        data = results["data"]

        # Table Varible
        table = PrettyTable(["Asset", "Price",  "1hr", "24hr", "7d"])

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
            

            price = quote["price"]
            volume = quote["volume_24h"]

            # Formatting data with Color Indicators
            if percent_change_1hr is not None:
                percent_change_1hr = round(percent_change_1hr, 2)
                if percent_change_1hr > 0:
                    percent_change_1hr = Back.GREEN + str(
                        percent_change_1hr) + "%" + Style.RESET_ALL
                else:
                    percent_change_1hr = Back.RED + str(
                        percent_change_1hr) + "%" + Style.RESET_ALL

            if percent_change_24hr is not None:
                percent_change_24hr = round(percent_change_24hr, 2)
                if percent_change_24hr > 0:
                    percent_change_24hr = Back.GREEN + str(
                        percent_change_24hr) + "%" + Style.RESET_ALL
                else:
                    percent_change_24hr = Back.RED + str(
                        percent_change_24hr) + "%" + Style.RESET_ALL

            if percent_change_7d is not None:
                percent_change_7d = round(percent_change_7d, 2)
                if percent_change_7d > 0:
                    percent_change_7d = Back.GREEN + str(
                        percent_change_7d) + "%" + Style.RESET_ALL
                else:
                    percent_change_7d = Back.RED + str(
                        percent_change_7d) + "%" + Style.RESET_ALL

            

            if volume is not None:
                volume_string = "{:,}".format(round(volume, 2))

            if market_cap is not None:
                market_cap_string = "{:,}".format(round(market_cap, 2))

            price_string = "{:,}".format(round(price, 2))

            # Table formatting
            table.add_row([name + " (" + symbol + ')',
                           local_symbol + price_string,
                           str(percent_change_1hr),
                           str(percent_change_24hr),
                           str(percent_change_7d)])

        print()
        print(table)
        print()
    except KeyError as key_ex:
        print("Error, please try again")
        coincap_ranker()


execute_coincap_ranker = True

# Future Value Predictor (Calculation : Gold,
# Or Stock market_cap * percentage_of_global_cap / available_supply )


def future_value():

    # BASE_URL = 'https://pro-api.coinmarketcap.com'
    GLOBAL_URL = (
        BASE_URL +
        '/v1/global-metrics/quotes/latest?convert=' +
        local_currency
    )
    try:
        request = requests.get(GLOBAL_URL, headers=headers, timeout=15)
        results = request.json()

        # print(json.dumps(results, sort_keys=True, indent=4))
        data = results["data"]

        encoding = 'utf-8-sig'

        total_market_cap = int(
            data["quote"][local_currency]
            ["total_market_cap"])
        string_total_market_cap = "{:,}".format(total_market_cap)

        # Table Headers found @
        # https://www.visualcapitalist.com/ +
        # all-of-the-worlds-money-and-markets-in-one-visualization-2022/
        table = PrettyTable(
            ["Name", "% total glo-cap", "11.5T(Gold)", "95.5T(Stocks)"])

        listing_url = (
            BASE_URL +
            "/v1/cryptocurrency/listings/latest?convert=" +
            local_currency
        )

        request = requests.get(listing_url, headers=headers, timeout=15)
        results = request.json()

        data = results['data']

        for currency in data:
            name = currency["name"]
            available_supply = currency["circulating_supply"]

            market_cap = currency['quote'][local_currency]["market_cap"]
            percentage_of_global_cap = float(market_cap) / total_market_cap

            # Calculation for future prices(Price is subject to change)
            gold_price = (
                12747000000000 *
                percentage_of_global_cap /
                available_supply
            )
            stock_market_price = (
                95500000000000 *
                percentage_of_global_cap /
                available_supply
            )

            # Formatting
            string_percentage_of_global_cap = str(
                round(percentage_of_global_cap * 100, 2)) + "%"
            string_gold_price = local_currency + \
                '{:,}'.format(round(gold_price, 2))
            string_stock_market_money = local_currency + \
                "{:,}".format(round(stock_market_price, 2))

            # Table
            table.add_row([name, string_percentage_of_global_cap,
                          string_gold_price, string_stock_market_money])

        print()
        print(table)
        print()
    except KeyError as key_ex:
        print("Error, please try again")
        future_value()


execute_future_value = True

# Clear text for function for terminal


def clear_text_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Terminal Menu


def display_Menu():
    print("Kurts Crypto Data Center")
    print()
    print("Select [1] for Global Market Data")
    print("Select [2] for Coin Listings Data ")
    print("Select [3] for Coin Quotes ")
    print("Select [4] for Top 100 Performing Crypto-Currencys")
    print("Select [5] for Future Value Predictor")
    print()
    print("Select [0] to Exit")


# Menu while loop
while True:
    clear_text_terminal()
    display_Menu()

    while True:
        keyboardValue = input()
        try:
            user_input = int(keyboardValue)
            break
        except ValueError as exc:
            print(f"Invalid input: {exc}")

    if user_input == 1 and execute_global_data:  # Global Data
        clear_text_terminal()
        global_market_data(local_currency, local_symbol)
        execute_global_data = False
        input("Press [Enter] to return to Menu")
        execute_global_data = True
    elif user_input == 2 and execute_coincap_listings:  # Listings Data
        clear_text_terminal()
        coincap_coin_listings(local_currency, local_symbol)
        execute_coincap_listings = False
        input("Press [Enter] to return to Menu")
        execute_coincap_listings = True
    elif user_input == 3 and execute_coincap_quotes:  # Quotes Data
        clear_text_terminal()
        coincap_quotes()
        execute_coincap_quotes = False
        input("Press [Enter] to return to Menu")
        execute_coincap_quotes = True
    elif user_input == 4 and execute_coincap_ranker:  # Crypto Ranker
        clear_text_terminal()
        coincap_ranker()
        input("Press [Enter] to return to Menu")
        execute_coincap_ranker = True
    elif user_input == 5:  # Future Value Predictor
        clear_text_terminal()
        future_value()
        execute_future_value = False
        input("Press [Enter] to return to Menu")
        execute_future_value = True
    elif user_input == 0:
        clear_text_terminal()
        print("Exiting the program...")
        break
    else:
        clear_text_terminal()
        print("Invalid option. Please select a valid option.")
        input("Press [Enter] to return to Menu")
