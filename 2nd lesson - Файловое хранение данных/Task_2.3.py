"""
2.3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с 
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

data_dict = {
    "data_list": ["Lenovo",
                  "Samsung",
                  "Asus"],
    "number": 100,
    "inner_dict": {'1€': 1,
                   '2€': 2,
                   '3€': 3}}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_dict, f_n, default_flow_style=True, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as f_n:
    CONTENT_FILE = yaml.load(f_n, Loader=yaml.FullLoader)
    print(CONTENT_FILE)

    if CONTENT_FILE == data_dict:
        print("Данные совпадают")
    else:
        print("Данные разные")