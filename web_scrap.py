from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

start_date = '2018-10-10'
end_date = str(datetime.now().strftime('%Y-%m-%d'))

stock = 'TSLA'

def get_stats(stock_data):
    return{
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }

def clean_data(stock_data, col):
    weekdays = pd.date_range(start = start_date, end = end_date)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label='tikcer')
    plt.xlabel("Date")
    plt.ylabel("Price, $")
    plt.title("Ticker: "+ticker)
    plt.show()

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))

stock_data = get_data(stock)
