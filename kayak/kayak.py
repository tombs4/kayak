import requests
# gets the API key so that it's not hard-coded into github
with open('c:\\users\\thoma\\kayak_api_key.txt', 'r') as f:
    key = f.read()
# latitude for Frederick MD
lat = "39.4143"
# longitude for Frederick MD
lon = "77.4105"
# the URL that will be used to get the data
url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}".format(lat,lon,key)
# prints the filled in URL for troubleshooting
print(url)
# get the response from the API
response = requests.get(url)
# show the response from the API
print(response.content)

# at time of writing this was throwing a 401 response
# b'{"cod":401, "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}'
# there's an error that indicates that it will take several hours for the API key to activate
# pushing this commit and going to bed