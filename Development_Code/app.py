import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests as rq
import yfinance as yf
from datetime import date

#Define Cryptos
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Solana = 'SOL-USD'

START = "2022-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#Yahoo finance tickers
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
SOL_DATA = yf.Ticker(Solana)

st.title('Cryto-AI-Advisor')

st.sidebar.title("Interactive Cryto App")

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

#add drop down 
cryto_selectbox = st.sidebar.selectbox(
    "Select a Cryptocurrency",
    ("BitCoin", "Ethereum", "Solana")
)   

data = load_data(cryto_selectbox)
#Add radio buttons
with st.sidebar:
   strategy_radio = st.radio(
   "Trading Strategy Model",
   ("Best Technical Indicators", "Strategy 1", "Strategy 2")
   )

st.markdown('**Cryptocurrency Name**')
st.write(cryto_selectbox)

#Trading Prices and Charts
if cryto_selectbox == "BitCoin":
        st.write('Current Trading price: ',BTC_Data)

if cryto_selectbox == "Ethereum":
        st.write('Current Trading price: ',ETH_Data)

if cryto_selectbox == "Solana":
        st.write('Current Trading price: ',SOL_DATA)

st.subheader('Raw data')
st.write(data.tail())