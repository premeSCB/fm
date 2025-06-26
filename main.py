
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm

ticker_symbol = 'AAPL'
data = yf.download(ticker_symbol)