from bs4 import BeautifulSoup
import requests
import json


urls = []
topics = []
data = []

def parse_page(url: str) -> dict:
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    r = requests.get(url, headers={'user-agent': user_agent})
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        related = soup.find('a', {'class':'ed0g1kj0'}).text
    except:
        related = None
    return related

def parse_bbc():
    url = r'https://www.bbc.com/sport'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    response = requests.get(url, headers={'user-agent': user_agent})
    soup = BeautifulSoup(response.text, 'lxml')
    page = soup.find('main', id='main-content')
    cards = page.find_all('div', {'class':'ssrcss-1phhpkj-PromoSwitchLayoutAtBreakpoints'})
    for card in cards:
        url = card.find('a').get('href')
        url = "https://www.bbc.com" + url
        urls.append(url)
        topic = parse_page(url)
        topics.append(topic)

def write_json(data: list) -> None:
    data = [{"url": urls[i], "topic": topics[i]} for i in range(5)]
    print(data)
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)



if __name__ == '__main__':
    parse_bbc()
    write_json(data)



#<a href="/sport/rugby-union" class="ssrcss-1ef12hb-StyledLink ed0g1kj0">Rugby Union</a>