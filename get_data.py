import requests
my_headers = {"x-api-key": "tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc"}
response = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace", headers=my_headers)
print(response.text)

