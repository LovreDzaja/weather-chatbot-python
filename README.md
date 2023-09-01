# ☀️ Weather Forecast Chatbot 🌧️

This is a simple weather forecast chatbot that provides current weather information for a given city using the OpenWeatherMap API.

## Usage

1. Replace 'YOUR_API_KEY' with your OpenWeatherMap API key in the `API_KEY` variable within the `get_weather` function.

2. To run the chatbot, execute the script in your terminal or code editor. It will continuously prompt you for input until you type 'exit' to quit.

3. You can ask the chatbot about the weather in a specific location by using phrases like:
   - "What's the weather like in [city]?"

4. The chatbot will provide the current temperature in Celsius and a brief description of the weather conditions for the specified city.

## Dependencies

- This chatbot uses the `requests` library to make HTTP requests to the OpenWeatherMap API. You can install it using pip:
  ```bash
  pip install requests
  ```
  
## Response Formatting

- The chatbot's responses are formatted using the following conventions:
  - **City Names** are displayed as regular text.
  - **Temperature** is displayed in **bold**.
  - **Weather Conditions** are displayed in *italics*.
  - Error messages are displayed in a different format for clarity.

## Exitting the chatbot

Simply type exit and click enter. Have fun coding. 😄
