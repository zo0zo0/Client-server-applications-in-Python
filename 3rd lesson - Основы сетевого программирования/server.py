#server
"""
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции сервера: принимает сообщение клиента;
формирует ответ клиенту; отправляет ответ клиенту; имеет параметры командной строки: -p <port> — TCP-порт для работы
(по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""

from socket import socket, AF_INET, SOCK_STREAM
import time
import json

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.bind(('', 7777))
SERV_SOCK.listen(5)

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        print(f'Получен запрос на соединение от клиента с адресом и портом: {ADDR}')
        TIMESTR = time.ctime(time.time()) + "\n"

        REC_MSG = CLIENT_SOCK.recv(1024)
        # JS_DEC = REC_MSG.decode('ascii')
        JS_DEC = REC_MSG.decode('utf-8')
        JS_DIC = json.loads(JS_DEC)
        print(f'Благополучно получено сообщение `{JS_DIC["user"]["status"]}` от {JS_DIC["user"]["account_name"]} - '
              f'{JS_DIC["time"]}')

        CLIENT_SOCK.send(TIMESTR.encode('utf-8'))
        #CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()