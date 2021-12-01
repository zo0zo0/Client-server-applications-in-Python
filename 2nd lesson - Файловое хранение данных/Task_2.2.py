"""
2.2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(dct):
    with open('orders.json') as f_n:
        data = json.load(f_n)
    data['orders'].append(dct)
    with open('orders.json', 'w', encoding='utf-8') as file_n:
        json.dump(data, file_n, indent=4, ensure_ascii=False)


order_dct = {'товар (item)': 'Lenovo Book',
                         'количество (quantity)': 50,
                         'цена (price)': 23000,
                         'покупатель (buyer)': 'Stanislav D.',
                         'дата (date)': "22.10.2020"
            }

write_order_to_json(order_dct)

with open('orders.json', encoding='utf-8') as f_n:
    print(f_n.read())
