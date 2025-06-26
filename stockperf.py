import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from scipy.stats import norm
from datetime import datetime

ticker_symbol = 'AAPL'
data = pd.read_csv("STOCK_US_XNAS_AAPL_excel.csv")

plt.figure(figsize=(10, 5))
plt.plot(data['Close'])
plt.title(f'{ticker_symbol} Historical Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.grid(True)
plt.show()

