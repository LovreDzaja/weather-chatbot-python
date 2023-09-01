import requests

# Replace with your OpenWeatherMap API key
API_KEY = '8233e90310c587f83e5d3e7bf29e2e6e'

def get_weather(city):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code == 200:
        #converter to celsius from Kelvin
        temperature = round((data['main']['temp']) - 273.15)
        weather_condition = data['weather'][0]['description']
        return f'The current temperature in {city} is {temperature}°C. The weather is {weather_condition}.'
    else:
        return 'I\'m sorry, I couldn\'t find the weather information for that location.'

def get_response(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    if 'weather' in words and 'in' in words:
        city_index = words.index('in') + 1
        if city_index < len(words):
            location = words[city_index]
            return get_weather(location)

    return 'I\'m not sure how to respond to that.'

# Testing the weather forecast chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_response(user_input)
    print("Bot: " + response)
