import pandas as pd
import pandas_datareader as pdr
import datetime 
stock_symbols = ['BAC']

def get__timeseries_of_stock(stock_name: str, start_date, end_date):
    return pdr.DataReader(stock_name, 'stooq', start_date, end_date)

def get__timeseries(stock_name: str, period_back: int):
    if(stock_name is None): 
        return "Invalid 'stock_name' parameter given"
    if(period_back is None): 
        return "Invalid 'period' parameter given"
    #date format: (2024, 1, 9)
    date_today = datetime.date.today() 
    date_week_ago = date_today - datetime.timedelta(period_back)
    start_date = date_week_ago
    end_date =  date_today
    return get__timeseries_of_stock(stock_name, start_date, end_date)