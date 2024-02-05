from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

base_router = APIRouter()

@base_router.get("/")
def read_root():
    return {"timeseries-processor": "root"} 