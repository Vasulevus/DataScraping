import requests
import re
import json
import sqlite3


def get_content2():
    url = 'https://www.lejobadequat.com/emplois'
    data = []
    response = requests.get(url)
    regex = re.findall(r'\<\w+\ [a-z]{2}\=\"\w+\-\d+\"\ \w+\=\"[a-zA-Z0-9\ \-\_\"\>\n]+\<a\ href="(\w+\:\/{2}w{3}.\w+\.[a-z]{3}[a-z0-9\/\-$]+).*[\s\<\>a-zA-Z0-9\=\"\_\-\'\/\à\!\:\.\é]+\"\w+\ \w+\-\d">(\D+)\<',response.text)
    return regex



def write_json(data: list) -> None:
    filename = "result.json"

    data = [
        {
            'Title': item[1],
            'Url': item[0]
        }
        for item in data
    ]

    with open(filename, mode='w') as f:
        json.dump(data, f, indent=4)


def write_sql(data: list) -> None:
    filename = "result.db"
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    SQL = """
    CREATE TABLE IF NOT EXISTS Jobs(
    [Id] INTEGER PRIMARY KEY,
    [Title] TEXT,
    [Url] TEXT
    )
    """
    cursor.execute(SQL)

    for item in data:
        cursor.execute(
            """
            INSERT INTO Jobs(Title,Url) VALUES(?,?)
            """, (item[1],item[0])
        )

    conn.commit()
    conn.close()




if __name__ == '__main__':
    write_json(get_content2())
    write_sql(get_content2())
