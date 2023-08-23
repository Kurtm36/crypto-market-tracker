"""
Back up api boiler plate
"""

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
GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(GLOBAL_URL, headers=headers)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]
