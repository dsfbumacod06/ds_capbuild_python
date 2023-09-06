import requests

url = 'https://globe-cosmosdb.azurewebsites.net/api/get-function?code=hbRTNx5pQ5zIsUrhLSYbNauONpzlJwUf2ow8sxcH_I7-AzFuS-8GTQ%3D%3D'

data = {
    "employeeID": 10000000,
    "source": "structured"
}

response = requests.post(url, json=data,)
print(response.text)
