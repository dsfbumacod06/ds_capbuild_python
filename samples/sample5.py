import requests

url = 'https://globe-cosmosdb.azurewebsites.net/api/set-function?code=JftdMwwpQvsoNOuKG5Q6xtBFY49zMz3jzONIKukkctzmAzFu1oaTqA%3D%3D'

data = {
    "employeeID": 10000000,
    "source": "structured"
}

response = requests.post(url, json=data,)
print(response.text)
