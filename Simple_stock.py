import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
         # Simple Stock Price App
         Retrieve the stock closing price and volume
         """)

# define ticker symbol
st.header('Enter the Company Code')
inputsymbol = 'AAPL'

tickerSymbol = st.text_area("Input", inputsymbol, height=10)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-4-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(""" 
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)

st.write(""" 
         ## Volume Price
         """)
st.line_chart(tickerDf.Volume)