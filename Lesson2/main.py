import xml.etree.ElementTree as ET
import json


def XmlParse():
    tree = ET.parse('New.xml') #парсимо дерево xml файлів
    root = tree.getroot()
    facts = []
    for f in root:
        #print(f.tag, f.attrib)
        for m in f:
            #print(m.tag, m.text)
            if m.tag == 'fact':
                facts.append(m.text)

    #print(facts)
        
    with open('cats.txt', mode='w') as f: #записуємо в новостворений файл
        f.write('\n'.join(facts))

def ParseXML():
    tree = ET.parse('New.xml')
    root = tree.getroot()
    facts = []
    for info in root.findall('info'): #знайти всі, які мають тег info
        fact = info.find('fact').text #в кожному рядку шукаємо текст факту
        facts.append(fact)
    with open('cats2.txt', mode='w') as f: #записуємо в новостворений файл
        f.write('\n'.join(facts))

def JSONParse():
    tree = ET.parse('New.xml')
    root = tree.getroot()
    facts = []
    for info in root.findall('info'): #знайти всі, які мають тег info
        fact = info.find('fact').text #в кожному рядку шукаємо текст факту
        facts.append({"fact":fact}) #список в json замісь array
    with open('cats.json', mode='w') as j:
        json.dump(facts, j, indent= 4) #завантажуємо у файл з відступом 4

def readJSON():
    with open('cats.json', mode='r') as r: #читаємо (завдяки режиму read або ж mode='r')
        data = json.load(r) #вантажимо
        print(data, type(data))

def compare():
    tree = ET.parse('New.xml')
    root = tree.getroot()
    facts = {}
    for index, info in enumerate(root.findall('info'), 1): #знайти всі, які мають тег info
        fact = info.find('fact').text #в кожному рядку шукаємо текст факту
        facts[index] = {"fact":fact} #додаємо ключ індексу
    print(facts, type(facts))
    with open('cats.json', mode='w') as j:
        json.dump(facts, j, indent= 4) #завантажуємо у файл з відступом 4
    with open('cats.json', mode='r') as r: #читаємо (завдяки режиму read або ж mode='r')
        data = json.load(r) #вантажимо
        print(data, type(data))

if __name__ == '__main__':
    XmlParse()
    ParseXML()
    JSONParse()
    readJSON()
    compare()