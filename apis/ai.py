import requests
import json
import os

PROMPT = """
Analyze this weather data and provide clothing recommendations in the following strict format:

[Time Period]

    Weather: [Temperature range]°C, feels like [Apparent temp range]°C, wind [speed range] km/h (gusts up to [max gust] km/h), humidity [range]%, [precipitation details].

    Top: [Clothing recommendations]

    Bottom: [Clothing recommendations]

    Accessories: [Recommendations]

    Footwear: [Recommendations]

Separate into Morning (00-08), Daytime (09-16), and Evening (17-23) periods. Use only bullet points (use "*" symbols). Exclude all commentary, explanations, and general tips. Respond in English.

Here is the weather data in json format: {0}
"""

def make_ai_request(weather_json: str):
    key = os.getenv("OPENROUTE_KEY")
    if not key:
        raise Exception("OPENROUTE_KEY not set")
    req = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.3-8b-instruct:free",
            "messages": [
                {
                    "role": "user",
                    "content": PROMPT.format(weather_json),
                }
            ]
        })
    )
    req.raise_for_status()
    response = req.json()
    return response["choices"][0]["message"]["content"]
