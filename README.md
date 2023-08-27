# Kurts Crypto Market Data App

The Crypto Market Data App is a Python application that provides real-time information provoided by coinmarket-cap API about various cryptocurrencies and their market performance. It fetches data from the CoinMarketCap API and displays it in a user-friendly format in the terminal.

## Features Overview
- Global Market Data: Get an overview of the global cryptocurrency market.
- Coin Listings Data: Display the latest data for all listed cryptocurrencies.
- Coin Quotes: Get the latest data for a specific cryptocurrency by its ticker symbol.
- Top 100 Performing Cryptocurrencies: Display a ranked list of top 100 cryptocurrencies based on different metrics.
- Future Value Predictor: Hypothetical future values of cryptocurrencies based on different market cap scenarios.

![]()
#### Global Market Data

#### Coin Listings

#### Coin Quotes 

#### Top 100 Performing Cryptocurrencys

#### Future Value Predictor


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

### Example Usage
- To view global market data, choose option 1.
- To get data for specific coins, select option 2.
- For coin quotes, choose option 3.
- To see the top 100 performing cryptocurrencies, select option 4.
- For future value predictions, choose option 5.