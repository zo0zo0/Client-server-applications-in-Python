# client
"""
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.
"""

import json
from socket import socket, AF_INET, SOCK_STREAM
import time

CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCK.connect(('localhost', 7777))


def form_msg(msg):
    client_msg = {"action": "presence",
                  "time": f"{time.asctime()}",
                  "type": "status",
                  "user": {
                      "account_name": "LoldH1hi",
                      "status": f"{msg}"
                  }
                  }
    js_msg = json.dumps(client_msg)
    # enc_msg = js_msg.encode('ascii')
    enc_msg = js_msg.encode('utf-8')

    return enc_msg


def msg_to_send(msg):
    CLIENT_SOCK.send(form_msg(msg))


try:
    while True:
        # msg_to_send()
        msg_to_send(input("Напиши сообщение: "))
        TIME_BYTES = CLIENT_SOCK.recv(1024)
        # print(f"Текущее время: {TIME_BYTES.decode('ascii')}")
        print(f"Текущее время: {TIME_BYTES.decode('utf-8')}")
finally:
    CLIENT_SOCK.close()
