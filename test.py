import requests

url = "https://api.twitterapi.io/twitter/user/info"
querystring = {"userName":"ram"}

headers = {"X-API-Key": "sorry"}

response = requests.get(url, headers=headers,params=querystring)

print(response.json())
