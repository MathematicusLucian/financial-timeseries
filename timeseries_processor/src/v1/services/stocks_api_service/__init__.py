from src.v1.services.stocks_api_service.stocks_api_interface import StocksApiInterface
from src.v1.services.stocks_api_service.implementation.stooq import StooqApiManager
from src.v1.services.stocks_api_service.implementation.nasdaq import NasdaqApiManager

stooq_api = StooqApiManager()
nasdaq_api = NasdaqApiManager()

async def get__stock_api(source: str) -> StocksApiInterface:
    if(source=="nasdaq"):
        return nasdaq_api
    return stooq_api
