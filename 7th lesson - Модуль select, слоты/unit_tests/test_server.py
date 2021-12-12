import unittest
import lesson_7.common.variables as variables
from lesson_7.server import process_client_msg

# корректные данные
ACTION_GOOD = variables.PRESENCE
USER_GOOD = 'Sergey'
PORT = variables.DEFAULT_PORT
TIME = 1.1
RESPONSE_GOOD = {variables.RESPONSE: 200}

# некорректные данные
USER_BAD = 'lolD'
RESPONSE_BAD = {
    variables.RESPONSE: 400,
    variables.ERROR: 'УПС, ошибочка...'
}


class TestServer(unittest.TestCase):
    def test_process_client_msg_correct(self):
        # Тест ответа на корректное сообщение от клиента
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: PORT,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_GOOD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_GOOD)

    def test_process_client_msg_not_user(self):
        # Тест ответа на корректное сообщение от неизвестного клиента
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: PORT,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)

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