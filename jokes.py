import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=es&format=txt"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception if the status is not 200
        return response.text
    except requests.RequestException as e:
        return "Me he quedado sin chistes... Déjame pensar un rato"
