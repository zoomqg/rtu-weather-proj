from dotenv import load_dotenv
from apis.ai import make_ai_request
from apis.geocode import geocode_location
from apis.weather import get_wether_json

load_dotenv()

print("[1/3] Input location:", end=" ")
location: str = input()
location_info = geocode_location(location)

print(f'[2/3]Getting weather for "{location_info.results[0].formatted_address}" today...')
weather_json = get_wether_json(
    latitude=location_info.results[0].geometry.location.lat,
    longitude=location_info.results[0].geometry.location.lng,
)

print(f'[3/3] Finding suitable outfit suggestions...')
print(make_ai_request(weather_json))