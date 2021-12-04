import os, sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from lesson_5.server import process_client_msg
import lesson_5.common.variables as variables

ACTION_GOOD = variables.PRESENCE
USER_GOOD = 'Sergey'
RESPONSE_GOOD = {variables.RESPONSE: 200}
PORT = variables.DEFAULT_PORT
TIME = 1.1

USER_BAD = 'Sanya'
RESPONSE_BAD = {
    variables.RESPONSE: 400,
    variables.ERROR: 'Алерт! Ошибка'
}

class TestServer(unittest.TestCase):

    def test_process_client_msg_not_port(self):
        # Тест ответа на сообщение клиента без параметра port
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)

    def test_process_client_msg_port(self):
        # Тест ответа на сообщение клиента c некорректным портом
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: 8080,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)

if __name__ == '__main__':
    unittest.main()