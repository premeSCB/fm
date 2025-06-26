import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from blackscholes import*


'''data = yf.download(ticker_symbol) --> dowloading from yf doesn't work because SCB blocks,
need to download stock data from marketwatch and copy into directory manually.
'''
ticker_symbol = 'AAPL'
data = pd.read_csv("STOCK_US_XNAS_AAPL_excel.csv")

#Calculate logarithmic returns & drift
log_returns = np.log(1+data['Close'].pct_change()) ##
u = log_returns.mean() 
var = log_returns.var()
drift = u - (0.5*var)

#Generating random variables
stdev = log_returns.std()
days = 300
trials = 100
Z = norm.ppf(np.random.rand(days, trials))
daily_returns = np.exp(np.array(drift) + np.array(stdev) * Z)

#Calculate price paths
price_paths = np.zeros_like(daily_returns)
price_paths[0] = data['Close'].iloc[-1] ##
for t in range(1, days):
    price_paths[t] = price_paths[t-1]*daily_returns[t]

print(price_paths)
#plot
plt.figure(figsize=[10,8])
plt.plot(price_paths)
plt.title('300 days, 1000 trials Monte Carlo Simulation for AAPL')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()

#comparison to black scholes 
stock_perf_data = data['Close']
put_data = []
for price in stock_perf_data:
    bsm = BlackScholesModel(S=price, K=100, T=1, r=0.05, sigma=0.2)
    put_price = bsm.put_option_price()
    put_data.append(float(put_price))

call_data = []
for price in stock_perf_data:
    bsm = BlackScholesModel(S=price, K=100, T=1, r=0.05, sigma=0.2)
    call_price = bsm.call_option_price()
    call_data.append(float(call_price))
    
## so many variables: ^ changing underlying price affect option price @ strike $100
    
# bsm = BlackScholesModel(S=100, K=100, T=1, r=0.05, sigma=0.2)
# print(f"Call Option Price: {bsm.call_option_price()}")
# print(f"Put Option Price: {bsm.put_option_price()}")