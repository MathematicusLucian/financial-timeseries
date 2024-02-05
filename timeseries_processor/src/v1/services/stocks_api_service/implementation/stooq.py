import datetime
import pandas
import pandas_datareader as pdr
import logging
from src.v1.services.stocks_api_service.stocks_api_interface import StocksApiInterface

class StooqApiManager(StocksApiInterface):

    async def get__timeseries_of_stock(self, stock_name: str, source: str, start_date, end_date) -> pandas.DataFrame:
        try:
            dataset = pdr.DataReader(stock_name, source, start_date, end_date)
            logging.info("Connection successful.")
            return dataset #pandas.core.frame.DataFrame
        except Exception as e:
            logging.info(f"Connection unsuccessful: {e}")

    async def get__timeseries(self, stock_name: str, source: str, period_back: int) -> pandas.DataFrame:
        if(stock_name is None): 
            return "Invalid 'stock_name' parameter given"
        if(period_back is None): 
            return "Invalid 'period' parameter given"
        #date format: (2024, 1, 9)
        date_today = datetime.date.today() 
        date_week_ago = date_today - datetime.timedelta(period_back)
        start_date = date_week_ago
        end_date =  date_today
        dataset = await self.get__timeseries_of_stock(stock_name, source, start_date, end_date)
        logging.info(type(dataset))
        return dataset
