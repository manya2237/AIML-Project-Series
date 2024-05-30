from fastapi import FastAPI, HTTPException, Request
import requests

app = FastAPI()

@app.post("/webhook/{city}")
async def webhook(request: Request):
    req = await request.json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')
    parameters = req.get('queryResult', {}).get('parameters', {})

    if intent == "GetWeather":
        city = parameters.get('geo-city')
        if city:
            return await get_weather(city)
        else:
            return {"fulfillmentText": "Please specify city by writing ,  weather in [city]."}

async def get_weather(city: str):
    OPENWEATHERMAP_API_KEY = "71b79f12be329bef660370d5b0580826"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return {"fulfillmentText": "Sorry, I couldn't fetch the weather information."}

    weather_data = response.json()
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    response_text = f"The current weather in {city} is {description} with a temperature of {temperature}°C."
    return {"fulfillmentText": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
