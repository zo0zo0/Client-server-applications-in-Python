'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''


def func_append(val):
    return f"b'{val}'"


word_list = ['attribute', 'класс', 'функция', 'type']

for el in word_list:
    try:
        print(eval(func_append(el)))
    except SyntaxError:
        print(f'Из-за использования кириллицы в слове "{el}" возникает ошибка. Невозможно записать в байтовом типе: '
              f'bytes can only contain ASCII literal characters')
