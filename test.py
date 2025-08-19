import requests

url = "https://api.twitterapi.io/twitter/user/info"
querystring = {"userName":"ram"}

headers = {"X-API-Key": "857f59e1a2354af0be65433b54da1309"}

response = requests.get(url, headers=headers,params=querystring)

print(response.json())
