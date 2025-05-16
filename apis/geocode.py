import requests
from dataclasses import dataclass
from typing import List
import os

@dataclass
class Location:
    lat: float
    lng: float

@dataclass
class Geometry:
    location: Location

@dataclass
class Result:
    formatted_address: str
    geometry: Geometry

@dataclass
class ApiResponse:
    results: List[Result]
    status: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            results=[
                Result(
                    formatted_address=result["formatted_address"],
                    geometry=Geometry(
                        location=Location(
                            lat=result["geometry"]["location"]["lat"],
                            lng=result["geometry"]["location"]["lng"]
                        )
                    )
                )
                for result in data["results"]
            ],
            status=data["status"]
        )

def geocode_location(location_str: str) -> ApiResponse:
    key = os.getenv("GOOGLE_GEOCODE_KEY")
    if not key:
        raise Exception("GOOGLE_GEOCODE_KEY not set")
    req = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={location_str}&key={key}")
    req.raise_for_status()
    response = ApiResponse.from_dict(req.json())
    return response if response.status == "OK" else Exception("Error happened with your request")