from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

start_date = '2018-10-10'
end_date = str(datetime.now().strftime('%Y-%m-%d'))

stock = 'TSLA'

def clean_data(stock_data, col):
    weekdays = pd.date_range(start = start_date, end = end_date)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
        print(clean_data(stock_data, 'Adj Close'))
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))

stock_data = get_data(stock)
