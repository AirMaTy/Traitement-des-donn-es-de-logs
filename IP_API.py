import requests

response = requests.get("http://ip-api.com/json/165.225.76.120").json()

print(response['query'])
print(response['status'])
print(response['country'])
print(response['countryCode'])
print(response['region'])
print(response['regionName'])
print(response['city'])
print(response['zip'])
print(response['lat'])
print(response['lon'])
print(response['timezone'])