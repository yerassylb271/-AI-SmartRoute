import requests


def get_weather(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code != 200:
        return {
            "temperature": "Unknown",
            "condition": "Unknown",
            "wind": 0
        }


    data = response.json()

    current = data["current_weather"]

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Cloudy",
        45: "Fog",
        51: "Light rain",
        61: "Rain",
        71: "Snow",
        95: "Thunderstorm"
    }


    return {

        "temperature": current["temperature"],

        "condition": weather_codes.get(
            current["weathercode"],
            "Unknown"
        ),

        "wind": current["windspeed"],

        "description": weather_codes.get(
            current["weathercode"],
            "Unknown"
        )
    }