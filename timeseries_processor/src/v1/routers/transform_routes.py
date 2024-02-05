# import logging
from fastapi import APIRouter, Depends, Body, Request
# from fastapi.responses import JSONResponse
# from typing import Union, Any
# import json
# from bson import ObjectId
# from pydantic import BaseModel
from src.v1.services.transform_service import transform

transform_router = APIRouter()

@transform_router.get("/time_series/{id_category}")
async def timeseries_monthly_avg(timeseries):
    data = await transform.get__timeseries_monthly_avg(timeseries)
    return data

@transform_router.get("/time_series/{id_category}")
async def timeseries_close(timeseries):
    data = await transform.get__timeseries_close(timeseries)
    return data