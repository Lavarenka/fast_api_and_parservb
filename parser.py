import requests


def parser_price(items):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'origin': 'https://www.wildberries.by',
        'priority': 'u=1, i',
        'referer': 'https://www.wildberries.by/catalog/200019326/detail.aspx?targetUrl=EX',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
        'x-captcha-id': 'Catalog 1|1|1740575047|AA==|ce7f35acb4db4ab6b2e57c80615ce797|4DGikq8AZRKA2A1m5J8SBV2NrbWZ2te1uIl6dswAIir',
    }

    response = requests.get(

        f'https://card.wb.ru/cards/v2/detail?appType=1&curr=byn&dest=-59202&hide_dtype=10&spp=30&ab_testing=false&nm={items}',
        headers=headers,
    )

    res = response.json()
    amount = res['data']['products'][0]['sizes'][0]['price']['total']

    # Преобразование в формат "руб"
    rubles = amount // 100  # Целая часть (рубли)
    kopecks = amount % 100  # Остаток (копейки)

    # Форматирование строки
    formatted_amount = f"{rubles},{kopecks:02d} руб"  # Используем :02d для добавления ведущего нуля, если нужно

    return formatted_amount


def parser_body(items_body):
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Referer': 'https://www.wildberries.by/catalog/293859675/detail.aspx',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"',
    }

    items_body = str(items_body)

    for url in range(1, 20):
        try:
            formatted_value = f"{url:02d}"
            link = f'https://basket-{formatted_value}.wbbasket.ru/vol{items_body[:-5]}/part{items_body[:-3]}/{items_body}/info/ru/card.json'
            response = requests.get(link, headers=headers)
            print(link)
            if response.status_code == 200 or response.status_code == 201:
                print('201')
                return response.json()

        except:
            print('no')


'60407528' 'https://basket-04.wbbasket.ru/vol604/part60407/60407528/info/ru/card.json'
'146341459' 'https://basket-10.wbbasket.ru/vol1463/part146341/146341459/info/ru/card.json'