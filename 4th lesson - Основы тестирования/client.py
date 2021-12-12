# client

from .variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, PORT
from .utils import get_message, send_message

import sys
import json
import socket
import time
import argparse


def create_presence_msg(port=DEFAULT_PORT, acc_name='Sergey'):
    message_output = {
        ACTION: PRESENCE,
        TIME: time.time(),
        PORT: port,
        USER: {
            ACCOUNT_NAME: acc_name
        }
    }
    return message_output


def server_process_answer(message_server):
    if RESPONSE in message_server:
        if message_server[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message_server[ERROR]}'
    raise ValueError


def client_main():
    for_parse = argparse.ArgumentParser()
    for_parse.add_argument('port', nargs='?', type=int, default=DEFAULT_PORT)
    for_parse.add_argument('address', nargs='?', type=str, default=DEFAULT_IP_ADDRESS)

    args_parse = for_parse.parse_args()

    try:
        server_port = args_parse.port
        server_address = args_parse.address
        if not (1024 < server_port < 65535):
            raise ValueError
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    trans_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trans_port.connect((server_address, server_port))
    message_to_server = create_presence_msg(server_port)
    send_message(trans_port, message_to_server)
    try:
        answer = server_process_answer(get_message(trans_port))
        print(f"Ответ => {answer}")
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    client_main()