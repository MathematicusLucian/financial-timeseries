import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mangum import Mangum
from src.v1.routers import api_router

logging.basicConfig(level = logging.INFO)

app = FastAPI(title='timeseries')
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(api_router, prefix="/v1")

handler = Mangum(app, lifespan="off")

if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')