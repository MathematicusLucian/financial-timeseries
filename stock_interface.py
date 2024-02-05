import pandas as pd
import pandas_datareader as pdr
import nasdaqdatalink
import datetime 
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
stock_symbols = ['BAC']
nasdaqdatalink.ApiConfig.api_key = API_KEY

def save__timeseries_csv(data):
    data.to_csv('data/timeseries.csv')

def read__timeseries_csv():
    df = pd.read_csv('data/timeseries.csv', header=0, index_col='Date', parse_dates=True)
    return df

def get__timeseries_of_stock(stock_name: str, source: str, start_date, end_date):
    if(source=="nasdaq"):
        stock_name_prefixed = "WIKI/" + stock_name
        return nasdaqdatalink.get(stock_name_prefixed, start_date=str(start_date), end_date=str(end_date))
    return pdr.DataReader(stock_name, source, start_date, end_date)

def get__timeseries(stock_name: str, source: str, period_back: int):
    if(stock_name is None): 
        return "Invalid 'stock_name' parameter given"
    if(period_back is None): 
        return "Invalid 'period' parameter given"
    #date format: (2024, 1, 9)
    date_today = datetime.date.today() 
    date_week_ago = date_today - datetime.timedelta(period_back)
    start_date = date_week_ago
    end_date =  date_today
    return get__timeseries_of_stock(stock_name, source, start_date, end_date)