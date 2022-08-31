import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests as rq
import yfinance as yf
from datetime import date
import matplotlib
import sys
import matplotlib.pyplot as plt
from urllib.request import urlopen
from dotenv import load_dotenv
import requests
from binance import Client
#from streamlit import image as Image
from PIL import Image

#Loading in files and creating variables
bitcoin_sma_df = pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/btc_sma.csv")
bitcoin_macd_df= pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/btc_macd.csv")
eth_sma_df = pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/eth_sma.csv")
eth_macd_df = pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/eth_macd.csv")
sol_sma_df = pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/sol_sma.csv")
sol_macd_df = pd.read_csv("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/sol_macd.csv")

bitcoin_sma_df = bitcoin_sma_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]
bitcoin_macd_df = bitcoin_macd_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]
eth_sma_df = eth_sma_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]
eth_macd_df = eth_macd_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]
sol_sma_df = sol_sma_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]
sol_macd_df = sol_macd_df[['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']]


btc_image = Image.open("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/btc.jpg")
eth_image = Image.open("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/eth.jpg")
sol_image = Image.open("RUT-VIRT-FIN-PT-03-2022-U-LOL/03-Projects/Project-03/sol.jpg")


# Setting up Binance API keys and client for data endpoints

load_dotenv()
BINANCE_API_KEY=os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY=os.getenv('BINANCE_SECRET_KEY')
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, tld='us')


#Add Title
st.title('Cryto Surfer')

#Add sidebar
st.sidebar.title("Interactive Cryto App")


#Define Cryptos
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Solana = 'SOL-USD'

TODAY = date.today().strftime("%Y-%m-%d")

#Yahoo finance tickers
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
SOL_Data = yf.Ticker(Solana)


btc_old = BTC_Data.history(period="1 day")
eth_old = ETH_Data.history(period="1 day")
sol_old = SOL_Data.history(period="1 day")

btc = yf.download(Bitcoin, TODAY)
eth = yf.download(Ethereum, TODAY)
sol = yf.download(Solana, TODAY)


#add drop down 
cryto_selectbox = st.sidebar.selectbox(
    "Select a Cryptocurrency",
    ("BitCoin", "Ethereum", "Solana")
)   

#Add radio buttons
with st.sidebar:
   strategy_radio = st.radio(
   "Trading Strategy Model",
   ("SMA", "MACD")
   )

st.markdown('**Cryptocurrency Name**')
st.write(cryto_selectbox)



#Trading Prices and Charts
if cryto_selectbox == "BitCoin":
        st.image(btc_image)
        st.write('Current Trading price: ',btc)
        
        if strategy_radio == "SMA":
            data = bitcoin_sma_df
            bitcoin_sma_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(bitcoin_sma_cstkplt)
        
        if strategy_radio == "MACD":
            
            data = bitcoin_macd_df
            bitcoin_macd_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(bitcoin_macd_cstkplt)
            #st.write(bitcoin_macd_df.tail())
           
if cryto_selectbox == "Ethereum":
        st.image(eth_image)
        st.write('Current Trading price: ',eth)
        #st.image(eth_image)
        if strategy_radio == "SMA":
            data = eth_sma_df
            eth_sma_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(eth_sma_cstkplt)
           
        if strategy_radio == "MACD":
            data = eth_macd_df
            eth_macd_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(eth_macd_cstkplt)
if cryto_selectbox == "Solana":
        st.image(sol_image)
        st.write('Current Trading price: ',sol)

        if strategy_radio == "SMA":
            data = sol_sma_df
            sol_sma_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(sol_sma_cstkplt)
        if strategy_radio == "MACD":
            data = sol_macd_df
            sol_macd_cstkplt = go.Figure(data=[go.Candlestick(x=data['open_time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
            st.plotly_chart(sol_macd_cstkplt)

