import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests as rq
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
from urllib.request import urlopen
#import sma_machinelearning.ipynb
#from sma_machinelearning.ipynb import *

st.title('Cryto-AI-Advisor')

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

#data = load_data(cryto_selectbox)

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
        st.write('Current Trading price: ',btc)
        #if strategy_radio == "SMA":
           # st.write(bitcoin_sma_strategy)
       # if strategy_radio == "MACD":
           # st.write(bitcoin_macd_strategy)
if cryto_selectbox == "Ethereum":
        st.write('Current Trading price: ',eth)

if cryto_selectbox == "Solana":
        st.write('Current Trading price: ',sol)



import plotly.graph_objects as go
b_strategy_plot = pd.DataFrame({
    "open":[5,6,7,8],
    "high":[7,8,9,10],
    "low":[4,5,6,7],
    "close":[6,7,8,9],
    "open_time":["08-22-2022", "08-23-2022", "08-24-2022","08-21-2022"]
})
bitcoin_trend_cstkplt = go.Figure(data=[go.Candlestick(x=b_strategy_plot['open_time'],
                open=b_strategy_plot['open'],
                high=b_strategy_plot['high'],
                low=b_strategy_plot['low'],
                close=b_strategy_plot['close'])])


st.plotly_chart(bitcoin_trend_cstkplt)




