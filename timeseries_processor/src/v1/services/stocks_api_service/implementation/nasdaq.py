import datetime
import logging
import nasdaqdatalink
from src.v1.services.stocks_api_service.stocks_api_interface import StocksApiInterface
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
stock_symbols = ['BAC']
nasdaqdatalink.ApiConfig.api_key = API_KEY

class NasdaqApiManager(StocksApiInterface):

    async def get__timeseries_of_stock(self, stock_name: str, source: str, start_date, end_date):
        try:
            stock_name_prefixed = "WIKI/" + stock_name
            dataset = nasdaqdatalink.get(stock_name_prefixed, start_date=str(start_date), end_date=str(end_date))
            logging.info("Connection successful.")
            return dataset
        except Exception as e:
            logging.info(f"Log in unsuccessful: {e}")

    async def get__timeseries(self, stock_name: str, source: str, period_back: int):
        if(stock_name is None): 
            return "Invalid 'stock_name' parameter given"
        if(period_back is None): 
            return "Invalid 'period' parameter given"
        #date format: (2024, 1, 9)
        date_today = datetime.date.today() 
        date_week_ago = date_today - datetime.timedelta(period_back)
        start_date = date_week_ago
        end_date =  date_today
        return await self.get__timeseries_of_stock(stock_name, source, start_date, end_date)