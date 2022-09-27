from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from starlette import status
from models import CityBikeStation, Address
from schema.station import AllCityBikeStationSchema


router = APIRouter()


class Status(BaseModel):
    status: bool


@router.post("/post_stations")
async def get_stations():
    url = f"https://wegfinder.at/api/v1/stations"

    response = httpx.get(url=url, verify=False)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    list_stations = response.json()
    orm_list = []
    for station in list_stations:
        if station["status"] == "aktiv":
            station["status"] = True
        else:
            station["status"] = False

        orm_list.append(CityBikeStation(station_id=station["id"],
                                                name=station["name"],
                                                active=station["status"],
                                                description=station["description"],
                                                boxes=station["boxes"],
                                                free_boxes=station["free_boxes"],
                                                free_bikes=station["free_bikes"],
                                                longitude=station["longitude"],
                                                latitude=station["latitude"],
                                                internal_id=station["internal_id"]))

    await CityBikeStation.bulk_create(orm_list)

    return list_stations


@router.get("/all_stations", response_model=List[AllCityBikeStationSchema])
async def get_station_addresses():
    stations_orm = await CityBikeStation.all().only('id', 'latitude', 'longitude')
    url = f"https://api.i-mobility.at/routing/api/v1/nearby_address"
    list_of_addresses = []
    for station in stations_orm:
        params = {
            "latitude": f"{station.latitude}",
            "longitude": f"{station.longitude}"
        }
        response = httpx.get(url=url, params=params, verify=False)

        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=response.status_code, detail=f"{response.text}")
        address = response.json()
        list_of_addresses.append(Address(longitude=address["data"]["coordinate"]["longitude"],
                                       lontitude=address["data"]["coordinate"]["latitude"],
                                       type=address["data"]["type"],
                                       name=address["data"]["name"],
                                       address_id=address["data"]["id"],
                                       station_id=station.id))
    if len(list_of_addresses) > 0:
        await Address.bulk_create(list_of_addresses)

    stations = await CityBikeStation.filter(free_bikes__gt=0) \
                                    .order_by("-free_bikes", "name").prefetch_related('addresses')

    return stations
