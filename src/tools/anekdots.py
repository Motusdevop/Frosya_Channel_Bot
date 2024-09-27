import requests
from bs4 import BeautifulSoup


def get_random() -> str:
    url = 'https://www.anekdot.ru/random/anekdot/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    topicboxes = soup.find_all(class_='topicbox')

    return topicboxes[1].find(class_='text').text


if __name__ == '__main__':
    print(get_random())
