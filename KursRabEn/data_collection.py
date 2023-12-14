import pandas_datareader.data as pdr
import yahoo_finance as yf

def get_stock_data(ticker,start,end,file):
    stock_data = pdr.get_data_yahoo(ticker, start, end)
    stock_data.to_csv(file)


get_stock_data("GC=F", "2017-01-01", "2020-12-31", "train.csv")
get_stock_data("GC=F", "2021-01-01", "2021-03-10", "test.csv")


print("Exit")
