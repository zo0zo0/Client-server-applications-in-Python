#server

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPOND_FAULT_IP_ADDRESS
from common.utils import get_message, send_message

import socket
import sys
import json
import argparse
import logging
import errors_user as errors_user

LOG_MAIN = logging.getLogger('server')


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
            # raise ValueError
            raise errors_user.PortError
    #except ValueError:
    except errors_user.PortError as port_error:
        LOG_MAIN.critical(f'Ошибка порта {args.listen_port}: {port_error}. Соединение закрывается')
        #print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    address_listen = args.a
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((address_listen, listen_port))
    transport.listen(MAX_CONNECTIONS)
    LOG_MAIN.info(f'Сервер был запущен. Порт подключений: {listen_port}, адрес прослушивания: {address_listen}')

    while True:
        client, client_address = transport.accept()
        LOG_MAIN.info(f'Соединение установлено с клиентом - {client_address}')
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            LOG_MAIN.info(f'Получено сообщение {message_from_client} от клиента {client_address}')
            response = process_client_msg(message_from_client)
            send_message(client, response)
            LOG_MAIN.info(f'Отправлено сообщение сервера {response} клиенту {client_address}')
            client.close()
        except json.JSONDecodeError:
            LOG_MAIN.error(f'Не удалось декодировать сообщение клиента {client_address}.')
            client.close()
        except errors_user.IncorrectDataRecivedError:
            LOG_MAIN.error(f'Принято некорректное сообщение от удалённого компьютера. {client_address}')
        '''except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()'''

if __name__ == '__main__':
    server_main()