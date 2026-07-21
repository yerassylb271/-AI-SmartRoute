import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_routes(routes, weather):

    prompt = f"""
You are an AI Smart City transportation assistant.

Current weather:

Temperature: {weather["temperature"]}°C
Condition: {weather["condition"]}
Description: {weather["description"]}
Wind: {weather["wind"]} m/s

Available routes:
"""

    for route in routes:

        prompt += f"""

Category: {route["category"]}
Transport: {route["name"]}
Distance: {route["distance"]} km
Time: {route["time"]} min
Price: {route["price"]} KZT
CO2: {route["co2"]} kg
Smart Score: {route["score"]}/10
"""

    prompt += """

Choose ONLY ONE best route.

Your answer MUST follow exactly this format:

Recommended: <transport>

Reason:
- reason 1
- reason 2
- reason 3

Keep the answer under 80 words.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent Smart City transportation AI."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3

        )

        return response.choices[0].message.content

    except Exception:

        # Choose the best route locally if AI is unavailable
        best = max(
            routes,
            key=lambda r: (r["score"], -r["time"])
        )

        return f"""
Recommended: {best["name"]}

Reason:
- Highest Smart Score ({best["score"]}/10)
- Best balance between travel time, cost and environmental impact
- Suitable for the current weather conditions

Summary:
Time: {best["time"]} min
Distance: {best["distance"]} km
Cost: {best["price"]} KZT
CO₂: {best["co2"]} kg
"""
