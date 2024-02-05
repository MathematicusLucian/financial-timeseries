# from fastapi import Request
from abc import abstractmethod
from datetime import datetime
# from typing import List, Any

class StocksApiInterface(object):
    # @property
    # def client(self):
    #     raise NotImplementedError

    # @property
    # def stock_api(self):
    #     raise NotImplementedError

    @abstractmethod
    async def get__timeseries_of_stock(self, stock_name: str, source: str, start_date: datetime, end_date: datetime):
        pass

    @abstractmethod
    async def get__timeseries(self, stock_name: str, source: str, period_back: int):
        pass