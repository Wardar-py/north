from fastapi import APIRouter
from api.v1.endpoints import citybike_api


api_router = APIRouter()
api_router.include_router(citybike_api.router, prefix="/citybike_api", tags=["City bike api"])
