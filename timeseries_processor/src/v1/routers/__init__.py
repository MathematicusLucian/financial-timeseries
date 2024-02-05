#-------------------
# Routers subpackage
#-------------------

from fastapi import APIRouter
from src.v1.routers.base_route import base_router
from src.v1.routers.crud_routes import crud_router
from src.v1.routers.transform_routes import transform_router

api_router = APIRouter()
api_router.include_router(base_router, prefix='', tags=["Root"])
api_router.include_router(crud_router, prefix='/stock_api', tags=["Crud"])
api_router.include_router(transform_router, prefix='/transform', tags=["Transform"])