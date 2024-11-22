from bs4 import BeautifulSoup
import re
import requests

def parse_xml():
    xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <library>
            <book>
                <title>To Kill a Mockingbird</title>
                <author>Harper Lee</author>
                <year>1960</year>
                <isbn>978-0-06-112008-4</isbn>
            </book>
            <book>
                <title>1984</title>
                <author>George Orwell</author>
                <year>1949</year>
                <isbn>978-0-452-28423-4</isbn>
            </book>
            <book>
                <title>The Great Gatsby</title>
                <author>F. Scott Fitzgerald</author>
                <year>1925</year>
                <isbn>978-0-7432-7356-5</isbn>
            </book>
        </library>
    """


    soup = BeautifulSoup(xml, features='xml')
    #book = soup.find('book')
    book = soup.findAll(string='The Great Gatsby')
    #print(book)
    title_regex = soup.findAll(string=re.compile('Kill|Great'))
    print(title_regex)
    books = soup.find_all('book')
    for book in books:
        title = book.find('title').text
        year = book.find('year').text
    isbn = soup.find('book').find('isbn').text
    print(isbn)


def parse_html():
    url = r'https://www.theguardian.com/uk/travel'

    response = requests.get(url)
    #with open('theguardian.html', 'w', encoding="utf-8") as f:
    #    f.write(response.text)

    with open('theguardian.html', 'w', encoding="utf-8") as f:
        text = f.read()

    soup = BeautifulSoup(text,'lxml')


if __name__ == "__main__":
    parse_xml()
    parse_html()