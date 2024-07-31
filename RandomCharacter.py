import requests
import random


ID = random.randint(0, 826)



response = requests.get(f"https://rickandmortyapi.com/api/character/{ID}")

while (response.json()['status'] == 'unknown'):
    ID = random.randint(0, 826)
    response = requests.get(f"https://rickandmortyapi.com/api/character/{ID}")

status = response.json()['status']
name = str({response.json()['name']})[2:-2]
image = {response.json()['image']}
location = response.json()['location']['name']