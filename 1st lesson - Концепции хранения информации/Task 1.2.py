'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''


def str_to_byte(list):
    for el in list:
        print(f' {bytes(el, encoding="utf-8")} with type: {type(bytes(el, encoding="utf-8"))} where name is "{el}" and '
              f'length = {len(bytes(el, encoding="utf-8"))} ')


list_with_elems = ["class", "function", "method"]
str_to_byte(list_with_elems)
