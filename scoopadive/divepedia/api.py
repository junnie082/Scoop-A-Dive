from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup


def check_jeju_shops():
    serviceKey = 'junnie082'
    encodedKey = '%2FnoWZKULUcFiE2qPjFRA8lMQzCcatH%2B16NIEYuEzAIpdSqPKDt0FsNoIX%2B5UCm1nC78fOqVkIZJya7IVgSq67g%3D%3D'
    decodedKey = '/noWZKULUcFiE2qPjFRA8lMQzCcatH+16NIEYuEzAIpdSqPKDt0FsNoIX+5UCm1nC78fOqVkIZJya7IVgSq67g=='
    serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

    # curl - X
    # 'GET' \
    # 'https://api.odcloud.kr/api/15045337/v1/uddi:cf70399f-9d4b-41ed-840b-820f27aa9480?page=1&perPage=10&serviceKey=%2FnoWZKULUcFiE2qPjFRA8lMQzCcatH%2B16NIEYuEzAIpdSqPKDt0FsNoIX%2B5UCm1nC78fOqVkIZJya7IVgSq67g%3D%3D' \
    # - H
    # 'accept: */*'

    shops = []
    url = 'https://api.odcloud.kr/api/15045337/v1/'
    model = 'uddi:cf70399f-9d4b-41ed-840b-820f27aa9480'
    returnType = 'json'

    url += model + '?page=' + str(1) + '&perPage=' + str(10) + '&returnType=' + str(returnType) + '&serviceKey=' + encodedKey
    res = requests.get(url).json()
    totalCount = res['totalCount']

    for page in range(1, totalCount+1):
        perPage = '4'
        url = 'https://api.odcloud.kr/api/15045337/v1/'
        url += model + '?page=' + str(page) + '&perPage=' + str(perPage) + '&returnType=' + str(
            returnType) + '&serviceKey=' + encodedKey
        res = requests.get(url).json()
        data = res["data"]
        for item in data:
            shops.append({"name": item['센터이름'], "location": item['위치'], "phone": item['연락처']})

    return shops



