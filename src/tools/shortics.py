import requests


def get_random():
    r = requests.get('https://shortiki.com/export/api.php?format=json&type=random&amount=5').json()
    return r[0]
