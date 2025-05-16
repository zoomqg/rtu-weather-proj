import requests
import json
URL = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m,apparent_temperature,relative_humidity_2m,precipitation_probability,precipitation,wind_speed_10m,wind_gusts_10m&timezone=auto&forecast_days=1"

def get_wether_json(latitude: float, longitude: float) -> str:
    req = requests.get(URL.format(latitude, longitude))
    req.raise_for_status()
    return json.dumps(req.json(), indent=2)