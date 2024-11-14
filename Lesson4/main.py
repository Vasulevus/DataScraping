import requests
import re

def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    regex = re.findall(r'\"\w+\ \w+\-\d">(\D+)\<',response.text)
    with open('jobs.txt', mode='w',encoding="utf-8") as f: #записуємо в новостворений файл
        f.write('\n'.join(regex))
    print(regex)

if __name__ == '__main__':
    get_content()