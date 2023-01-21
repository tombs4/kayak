import requests
import json
import config

# latitude for Frederick MD
fred = config.config() 
print(fred.lat)
# longitude for Frederick MD
print(fred.long)

# using weather.gov API because it's free.
url = f"https://api.weather.gov/points/{fred.lat},{fred.long}"
# prints the filled in URL for troubleshooting
print(url)
# get the response from the API
response = requests.get(url)
# show the response from the API
# print(response.json())

# there should probably be a test for the below response 
# to verify that it's returning a real result
jsonresponse = response.json()
json_pretty = json.dumps(jsonresponse, indent=4)
# print(json_pretty)
# print(jsonresponse)

# used to get the properties in an easy-to-read format
# json_output = open("c:\\users\\thoma\\Git\\kayak\\json_response.json", "w")
# json_output.write(json_pretty)

# response = json.loads(jsonresponse)
# print(jsonresponse.items())
forecast_api_url = jsonresponse["properties"]["forecastHourly"]
print(forecast_api_url)

forecast_response = requests.get(forecast_api_url)
print(forecast_response.status_code)
if forecast_response.status_code == 200:
    json_output = open("c:\\users\\thoma\\Git\\kayak\\forecast_json.json", "w")
    json_output.write(json.dumps(forecast_response.json(), indent=4))
else:
    print("\n\nthat didn't work")

# well, the good news is that I found the data that I need in the 
# forecast_json.json file. Now i just need to figure out the appropriate algorithm
# for determining when it will be good to go kayaking in the next few days
