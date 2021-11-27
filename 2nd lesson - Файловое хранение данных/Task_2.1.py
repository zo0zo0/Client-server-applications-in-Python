"""
2.1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
 info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в
виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()
"""

import csv


def get_data(txt_lst):
    os_prod_list = []  # «Изготовитель системы»
    os_name_list = []  # «Название ОС»
    os_code_list = []  # «Код продукта»
    os_type_list = []  # «Тип системы»
    main_data = [['Изготовитель системы',
                  'Название ОС',
                  'Код продукта',
                  'Тип системы']]
    for file in txt_lst:
        handle = open(f'{file}', encoding='windows-1251')
        for line in handle:
            if 'Изготовитель системы' in line:
                os_prod_list.append(line.replace("\n", "").replace("Изготовитель системы:             ", ""))
            elif 'Название ОС' in line:
                os_name_list.append(line.replace("\n", "").replace("Название ОС:                      ", ""))
            elif 'Код продукта' in line:
                os_code_list.append(line.replace("\n", "").replace("Код продукта:                     ", ""))
            elif 'Тип системы' in line:
                os_type_list.append(line.replace("\n", "").replace("Тип системы:                      ", ""))
        handle.close()

    for _ in range(len(txt_lst)):
        main_data.append([
            os_prod_list[_],
            os_name_list[_],
            os_code_list[_],
            os_type_list[_]
        ])
    return main_data


def write_to_csv(file, data):
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for new_row in data:
            f_n_writer.writerow(new_row)


res_list = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
write_to_csv('file_for_task-2_1.csv', res_list)

with open('file_for_task-2_1.csv') as f_n:
    print(f_n.read())
