import requests
from bs4 import BeautifulSoup

def check_major():
    majors = []
    url = "https://www.seoultech.ac.kr/univ/univ/intro/"
    res = requests.get(url)
    xml = res.text

    soup = BeautifulSoup(xml, 'html.parser')
    data = soup.find_all('li')

    for item in data:
        res = item.find('a', {'target': "_blank"})
        if res != None:
            if res.text != 'ENG' and res.text != 'search':
                majors.append(res.text)

    return majors