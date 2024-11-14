import requests


def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    get_content()