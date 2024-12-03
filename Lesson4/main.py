#import requests
import re

def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    regex = re.findall(r'\"\w+\ \w+\-\d">(\D+)\<',response.text)
    with open('jobs.txt', mode='w',encoding="utf-8") as f: #записуємо в новостворений файл
        f.write('\n'.join(regex))
    print(regex)

def get_content2():
    regex = re.findall(r'^(\d+)-(\d{2})-(\d)$', "7440-44-0")
    print(regex)

if __name__ == '__main__':
    get_content2()