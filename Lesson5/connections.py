import csv
import json
import xml.etree.ElementTree as ET
import sqlite3


def write_csv(data: list) -> None:
    filename = 'output.csv'

    with open(file=filename,mode="w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['First Name','Last Name', 'Weight', 'IsMale'])
        writer.writerows(data)

def write_json(data: list) -> None:
    filename = 'output.json'

    data = [
        {
            'firstName': item[0],
            'lastName': item[1],
            'weight': item[2],
            'isMale': item[3]
        }
        for item in data
    ]

    with open(filename, mode='w') as f:
        json.dump(data, f, indent=4)


def write_xml(data: list) -> None:
    filename = 'output.xml'

    root = ET.Element('People')
    for item in data:
        person = ET.SubElement(root, 'Person')
        ET.SubElement(person, 'firstName').text = item[0]
        ET.SubElement(person, 'lastName').text = item[1]
        ET.SubElement(person, 'weight').text = str(item[2])
        ET.SubElement(person, 'isMale').text = str(item[3])

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
        
def write_sql(data: list) -> None:
    filename = 'output.db'

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    SQL = """
    CREATE TABLE IF NOT EXISTS People (
    [ID] INTEGER PRIMARY KEY,
    [Firstname] TEXT,
    [LastName] TEXT,
    [WEIGHT] INT,
    [IsMale] BOOLEAN 
    )
    """
    cursor.execute(SQL)

    for item in data:
        cursor.execute(
            """
            insert into People(Firstname,Lastname,WEIGHT,IsMale)
            values(?,?,?,?)
            """, (item[0],item[1],item[2],item[3])
        )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    example = [
        ["Tom", "Smith", 80, True],
        ["Alice", "Johnson", 92, False],
        ["Bob", "Williams", 75, True],
        ["Emma", "Brown", 88, False],
        ["David", "Jones", 107, True]
    ]
    write_csv(example)
    write_json(example)
    write_xml(example)
    write_sql(example)