import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from scipy.stats import norm
from datetime import datetime
from blackscholes import*

# Example for delta and 
range_start = 80
range_stop = 120
no_of_nums = 100
stock_prices = np.linspace(range_start, range_stop, no_of_nums)
deltas = []
for price in stock_prices:
    deltas.append(BlackScholesGreeks(S=price, K=100, T=1, r=0.05, sigma=0.2).delta_call())

plt.figure(figsize=(10, 5))
plt.plot(stock_prices, deltas)
plt.title('Delta of a Call Option as Underlying Price Changes')
plt.xlabel('Stock Price')
plt.ylabel('Delta')
plt.grid(True)
plt.show