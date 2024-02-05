import pandas as pd

def save__timeseries_csv(data):
    data.to_csv('./data/timeseries.csv')

def read__timeseries_csv():
    df = pd.read_csv('./data/timeseries.csv', header=0, index_col='Date', parse_dates=True)
    return df