# Imports of OS and API libraries

import os
from dotenv import load_dotenv
import requests
from binance import Client
import pandas as pd
import numpy as np
# Setting up Binance API keys and client for data endpoints
load_dotenv()
BINANCE_API_KEY=os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY=os.getenv('BINANCE_SECRET_KEY')
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, tld='us')

# Fetching Bitcoin USD data from June 2017 to June 2022 for the interval of 1-Day
bitcoin_data = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "01 Jun, 2017", "24 Aug, 2022")
