#server

from .variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPOND_FAULT_IP_ADDRESS
from .utils import get_message, send_message

import socket
import sys
import json
import argparse


def process_client_msg(client_message):
    if ACTION in client_message and client_message[ACTION] == PRESENCE and TIME in client_message \
            and USER in client_message and client_message[USER][ACCOUNT_NAME] == 'Sergey':
        return {RESPONSE: 200}
    return {
        RESPOND_FAULT_IP_ADDRESS: 400,
        ERROR: 'Bad Request'
    }


def server_main():
    print('Сервер погнал')
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', type=int, default=DEFAULT_PORT)
    arg_parser.add_argument('-a', type=str, default='')
    args = arg_parser.parse_args()

    try:
        listen_port = args.p
        if not(1024 < listen_port < 65535):
            raise ValueError
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    address_listen = args.a
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((address_listen, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_msg(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    server_main()