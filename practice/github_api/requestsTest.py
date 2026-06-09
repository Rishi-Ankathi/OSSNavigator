import requests

url = "https://api.github.com/repos/fastapi/fastapi"

response = requests.get(url)

print(response.status_code)

data = response.json()

#print(data.keys())
#print(data['owner'].keys())
print(data['owner']['login'])