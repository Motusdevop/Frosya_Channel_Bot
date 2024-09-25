import requests


def get_url_photo():
    data = requests.get('https://api.thecatapi.com/v1/images/search').json()

    url = data[0]['url']

    return url
