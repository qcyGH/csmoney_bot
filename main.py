from urllib.request import urlcleanup
from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

def collect_data(weapont_type=2, minPrice=2000):
    # response = requests.get(
    #     url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=0&type=2&withStack=true',
    #     headers={'user-agent': f'{ua.random}'}
    # )
    
    # with open('result.json', 'w', encoding="utf-8") as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    batch_size = 60
    result=[]
    count = 0

    while True:
        # цикл, который формерует ссылку
        for item in range(offset, offset + batch_size, 60):

            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&isStore=true&limit=60&maxPrice=10000&minPrice={minPrice}&offset={item}&quality=fn&type={weapont_type}&withStack=true'
            # отправляем запрос
            response = requests.get(
            url=url,
            headers={'user-agent': f'{ua.random}'}
            )

            offset += batch_size

            #получаем данные
            data = response.json()
            items = data.get('items')
            error = data.get('error')
            # if error == 2:
            #     print('К сожалению, ничего не найдено. Попробуйте позже!')
            #забираем позиции, которые удовлетворяют требования
            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')
                    item_img = i.get('img')
                    
                    # формируем словарь из данных
                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'img': item_img,
                            'overprice': item_over_price,
                            'item_price': item_price
                        }
                    )

        count += 1
        print(f'Page #{count}')
        print(item_3d)
        print(item_img)

        if len(items) < 60:
            break

    with open('result.json', 'w', encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False) 

    print(len(result))                   

def checking_error(weapont_type=2, minPrice=2000):

            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&isStore=true&limit=60&maxPrice=10000&minPrice={minPrice}&offset=0&quality=fn&type={weapont_type}&withStack=true'
            # отправляем запрос
            response = requests.get(
            url=url,
            headers={'user-agent': f'{ua.random}'}
            )

            #получаем данные
            data = response.json()
            items = data.get('items')
            error = data.get('error')
            count_items = 0
            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    count_items += 1

            if error == 2 or count_items == 0:
                return 2

def main():
    collect_data()

if __name__ == '__main__':
    main()    