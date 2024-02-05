import logging
from fastapi import APIRouter, Depends #, Body, Request
# from typing import Union, Any
import json
# from bson import ObjectId
# from pydantic import BaseModel
from src.v1.services.stocks_api_service.stocks_api_interface import StocksApiInterface
from src.v1.services.stocks_api_service import get__stock_api

crud_router = APIRouter()

@crud_router.get("/time_series/{stock_name}/{source}/{period_back}")
async def timeseries(stock_name: str, source: str, period_back: int, stocks_api: StocksApiInterface = Depends(get__stock_api)):
    timeseries = await stocks_api.get__timeseries(stock_name, source, period_back)
    response = timeseries.to_json(orient="records")
    parsedResponse = json.loads(response)
    return parsedResponse