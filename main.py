from dotenv import load_dotenv
from apis.ai import make_ai_request
from apis.geocode import geocode_location
from apis.weather import get_wether_json
from utils.json import JsonProcessor
from datetime import datetime


load_dotenv()

print("[1/3] Input location:", end=" ")
location: str = input()
location_info = geocode_location(location)
location_name = location_info.results[0].formatted_address
print(f'[2/3] Getting weather for "{location_name}" today...')
weather_json = get_wether_json(
    latitude=location_info.results[0].geometry.location.lat,
    longitude=location_info.results[0].geometry.location.lng,
)

print(f'[3/3] Finding suitable outfit suggestions...')
response = make_ai_request(weather_json=weather_json, location_name=location_name)
print("Here are the outfit suggestions:")
print(response)

json_reader = JsonProcessor("results.json", capacity=3)
json_reader.read_data()
json_reader.hash_table.insert(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), response)
json_reader.save_data()

print("Results saved to results.json\n")
print("Do you want to see the last 3 requests? (y/n)")
if input().lower() == "y":
    json_reader.hash_table.print_all()