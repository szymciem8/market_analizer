import yfinance as yf

tsla = yf.Ticker("TSLA")
print(tsla.major_holders)
