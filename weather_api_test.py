import urllib.request
import json
import requests
# API KEY
with open("dark_sky_api_key.txt", "r") as myfile:
    api_key = myfile.readlines()


lat = 42.3601
long = 71.0589

base_url = 'https://api.darksky.net/forecast/'
url = base_url + api_key[0][:-1] + '/' + str(lat) + ','+str(long)
print(url)

response = requests.get(url)
json_data = json.loads(response.text)


print(json_data.daily())
