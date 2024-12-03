from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import date

names = []
prices = []
shops = []
urls = []
data = []
unique_lists = []

def write_sql() -> None:
    filename = 'data.db'

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    SQL = """
    CREATE TABLE IF NOT EXISTS Parse (
    [ID] INTEGER PRIMARY KEY,
    [Name] TEXT,
    [Url] TEXT,
    [Shop] TEXT,
    [Price] TEXT,
    [Date] DATE
    )
    """
    cursor.execute(SQL)

    for item in unique_lists:
        cursor.execute(
            """
            INSERT INTO Parse(Name,Url,Shop,Price,Date)
            values(?,?,?,?,?)
            """, (item[0],item[1],item[2],item[3],item[4])
        )
    conn.commit()
    conn.close()

def parse_hotline():
    url = r'https://hotline.ua/ua/computer/igrovye-pristavki/'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    response = requests.get(url, headers={'user-agent': user_agent})
    soup = BeautifulSoup(response.text, 'lxml')
    page = soup.find('div', {'class':'list-body__content'})
    cards = page.findAll('div',{'class':'list-item--row'})
    
    for card in cards:
        name = card.find('a',{'class':'item-title'}).text.strip(' \t\n\r')
        url = 'https://hotline.ua' + card.find('a',{'class':'btn--orange'}).get('href')
#        page = parse_page(url)
#       pages.append(url)
        r = requests.get(url, headers={'user-agent': user_agent})
        soup = BeautifulSoup(r.text, 'lxml')
        lines = soup.findAll('div',{'class':'list__item'})
        for line in lines:
            price = line.find('span',{'class':'price__value'}).text.replace('\u00a0', '')
            names.append(name)
            prices.append(price)
            shop = line.find('a',{'class':'shop__title'}).text.strip(' \t\n')
            shop = shop.encode().decode('utf-8')
            shops.append(shop)
            url = 'https://hotline.ua' + line.find('a',{'class':'price-block__buy-shop'}).get('href')
            urls.append(url)
        for name, url, shop, price in zip(names,urls,shops,prices):
            new = []
            new.append(name)
            new.append(url)
            new.append(shop)
            new.append(price)
            new.append(date.today())
            data.append(new)
    for lst in data:
        if lst not in unique_lists:
            unique_lists.append(lst)
    write_sql()






if __name__ == '__main__':
    parse_hotline()




