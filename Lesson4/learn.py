import requests


def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    print(response.text)

def post_content():
    url = 'https://www.lejobadequat.com/emplois'
    payload = {"action":"facetwp_refresh","data":{"facets":{"recherche":[],"ou":[],"type_de_contrat":[],"fonction":[],"load_more":[2]},"frozen_facets":{"ou":"hard"},"http_params":{"get":[],"uri":"emplois","url_vars":[]},"template":"wp","extras":{"counts":True,"sort":"default"},"soft_refresh":1,"is_bfcache":1,"first_load":0,"paged":2}}
    response = requests.post(url,json=payload)
    print(response.status_code, response.text)


def use_headers():
    url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/'
    response = requests.get(url)
    print(response.text)

if __name__ == '__main__':
    #get_content()
    #post_content()
    use_headers()