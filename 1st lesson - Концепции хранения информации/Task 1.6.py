'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

import locale

print(locale.getpreferredencoding())

word_lst = ['сетевое программирование', 'сокет', 'декоратор']
test_file = open('test_file.txt', 'w', encoding='utf-8')
for el in word_lst:
    test_file.write(f'{el}\n')
print(test_file.encoding)
test_file.close()
print(type(test_file))


with open('test_file.txt', encoding='utf-8') as f_n:
    for line in f_n:
        print(line, end='')
    print()


