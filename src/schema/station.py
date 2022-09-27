from typing import List, Optional
from pydantic import BaseModel, condecimal
from tortoise.contrib.pydantic import PydanticModel


class CityBikeStationSchema(BaseModel):
    station_id: int
    name: str
    status: bool
    description: str
    boxes: int
    free_boxes: int
    free_bikes: int
    longitude: condecimal(max_digits=50, decimal_places=15)
    latitude: condecimal(max_digits=50, decimal_places=15)
    internal_id: int


class Address(BaseModel):
    name: str


class AllCityBikeStationSchema(PydanticModel):
    station_id: int
    name: str
    active: bool
    description: str
    boxes: int
    free_boxes: int
    free_bikes: int
    free_ratio: float
    coordinates: list
    addresses: Optional[List[Address]]
