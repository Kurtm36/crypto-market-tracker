# Kurts Crypto Market Data App

The Crypto Market Data App is a Python application that provides real-time information provoided by coinmarket-cap API about various cryptocurrencies and their market performance. It fetches data from the CoinMarketCap API and displays it in a user-friendly format in the terminal.

## Features Overview
- Global Market Data: Get an overview of the global cryptocurrency market.
- Coin Listings Data: Display the latest data for all listed cryptocurrencies.
- Coin Quotes: Get the latest data for a specific cryptocurrency by its ticker symbol.
- Top 100 Performing Cryptocurrencies: Display a ranked list of top 100 cryptocurrencies based on different metrics.
- Future Value Predictor: Hypothetical future values of cryptocurrencies based on different market cap scenarios.

![Main Menu](/images/main-menu.png)

--- 

#### Global Market Data
This function provides insights into the overall state of the cryptocurrency market, including the total market capitalization, trading volume, Bitcoin dominance, and Ethereum dominance.

![Global Market Data](/images/global-market-data.png)

#### Coin Listings
This function provides essential information about various cryptocurrencies, including their names, symbols, prices, 24-hour changes, 7-day changes, 30-day changes, and market capitalizations.

![Global Market Data](/images/coincap-listings.png)

#### Coin Quotes 
This function provides detailed information about the requested cryptocurrency, including its name, symbol, price, 24-hour change, 7-day change, 30-day change, and market capitalization.

![Coincap Quotes](/images/coincap-quotes.png)
![Coincap Quotes Return](/images/coincap-quotes-results.png)

#### Top 100 Performing Cryptocurrencys
This function fetches and interactively displays real-time ranking data for cryptocurrencies using the API. This function provides a comprehensive overview of the top 100 cryptocurrencies with color indictiors which are ranked based on various criteria, including market cap, 24-hour trading volume, 24-hour percent change, and 7-day change.

![Coincap Quotes](/images/top-100-menu.png)
![Coincap Quotes](/images/top-100-table.png)

#### Future Value Predictor
This function provoids hypothetical future values of cryptocurrencies based on different market cap scenarios such as Gold Market cap and the stock exchange market cap. THIS IS NOT FINANCIAL ADVICE !.

![Coincap Quotes](/images/future-value.png)

### Example Usage
- To view global market data, choose option 1.
- To get data for specific coins, select option 2.
- For coin quotes, choose option 3.
- To see the top 100 performing cryptocurrencies, select option 4.
- For future value predictions, choose option 5.

### Future features 
- In the future I would like to add a trading algorithm
- I would also like to add wallet function
- I would also like to export the data to ether Google Sheets or Win Excel.

---

## Requirements
- Python 3.x (I used Python 3.11)
- A valid CoinMarketCap API key , You can use the current API key but if you'd like you can download a free API key @ [CoinMarket Cap API](https://coinmarketcap.com/api/)
- Required Python libraries:
    - requests
    - json
    - os
    - locale
    - Datetime
    - Prettytable
    - Colorama

## Getting Started 
Follow these steps to set up and run my Crypto Market Data App on your local machine .

1. Clone the repository to your local machine   
``` git clone https://github.com/Kurtm36/crypto-market-tracker.git```

2.  Navigate to the project directory
   
    ```cd crypto-market-tracker```

3. Install the required Python libraries using pip

    ```pip install -r requirements.txt```

### Configuration

1. Open the `env.py` file in the project directory.
2. Replace `API_KEY` with your actual CoinMarketCap API key.
3. Save the file.

## Running the App
1. Execute the run.py file

    ```python3 run.py ```

2. The terminal will display the main menu. Choose an option by entering the corresponding number and pressing Enter.  

3. Follow the on-screen prompts to explore different features of the app.


## Deployment 
This project was deployed using Code institutes mock terminal for heroku 
- Steps for deployment 
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbacks for Python and NodesJS in that order 
  - Link the Heroku app to the repository
  - Click on deploy 

### Testing 
- I ran my program through the CI Python linter and recieved the  all clear with no errors found  

![Coincap Quotes](/images/python-linter.png)

- I tested different inputs and invalid inputs to see If I could break my program.
- I tested the App on command prompt aswell as other terminals 

### Bugs
- In coincap_ranker_func.py Price is matching market_cap (solved. If statements LN.97 & LN.100 had swaped varibles 
i.e market_cap in volume and volume in market_cap)

- In coincap_listing/quotes_func.py percent changes were appearing as EURO and not percent (solved. Corrected formatting on string_percent etc)

- In future_value_func.py - I had to use encoding = 'utf-8-sig' to solve a issue with api not iterateing through the data

- In future_value_func.py - I was using a "total_supply" instead of "circulating supply" for avaible_supply 

### Credits 
- This video helped me get set up with CoinmarketCap API [Beginner's Guide to the CoinMarketCap API](https://www.youtube.com/watch?v=f3GfkvfpVAE)

- Love sandwiches by Codeinstitute helped me understand how API's work.

- My mentor Aleksei Konovalovksi for his advice and guidance.
