'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
'''


def print_func(elems_lst):
    for el in elems_lst:
        print(f'Значение {el} с типом {type(el)}')
    print('---------------')


def byte_encode_func(val):
    lst = []
    for el in val:
        lst.append(el.encode('utf-8'))
    return lst


def byte_decode_func(val):
    lst = []
    for el in val:
        lst.append(el.decode('utf-8'))
    return lst


word_list = ['разработка', 'администрирование', 'protocol', 'standard']
print_func(word_list)
word_list = byte_encode_func(word_list)
print_func(word_list)
word_list = byte_decode_func(word_list)
print_func(word_list)
