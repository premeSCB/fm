
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm

ticker_symbol = 'AAPL'
#data = yf.download(ticker_symbol)
data = pd.read_csv("STOCK_US_XNAS_AAPL.csv")

#Calculate logarithmic returns & drift
log_returns = np.log(1+data['Close'].pct_change()) ##
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5*var)

#Generating random variables
stdev = log_returns.std()
days = 50
trials = 100
Z = norm.ppf(np.random.rand(days, trials))
daily_returns = np.exp(np.array(drift) + np.array(stdev) * Z)

#Calculate price paths
price_paths = np.zeros_like(daily_returns)
price_paths[0] = data['Close'].iloc[-1] ##
for t in range(1, days):
    price_paths[t] = price_paths[t-1]*daily_returns[t]

#plot
plt.figure(figsize=[10,8])
plt.plot(price_paths)