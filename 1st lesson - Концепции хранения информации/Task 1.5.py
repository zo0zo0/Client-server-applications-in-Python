'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
кириллице.
'''

import subprocess
import chardet

resources_ping_value = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for arg in resources_ping_value:
    go_and_ping = subprocess.Popen(arg, stdout=subprocess.PIPE)
    cycle = 0
    for line in go_and_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if cycle > 3:
            break
        cycle += 1
