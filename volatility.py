import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from scipy.stats import norm
from datetime import datetime

ticker_symbol = 'AAPL'
data = pd.read_csv("STOCK_US_XNAS_AAPL_excel.csv")

def calculate_historical_volatility(stock_data, window=252):
    log_returns = np.log(data['Close'] / data['Close'].shift(1))
    volatility = np.sqrt(window) * log_returns.std()
    return volatility

stock_volatility = calculate_historical_volatility(data)
print(f"{ticker_symbol} Historical Volatility: {stock_volatility}")