import unittest
import lesson_7.common.variables as variables
from lesson_7.client import create_presence_msg, server_process_answer

# корректные данные
ACTION_GOOD = variables.PRESENCE
USER_GOOD = 'Sergey'
PORT = variables.DEFAULT_PORT
TIME = 1.1
RESPONSE_GOOD = {variables.RESPONSE: 200}
MESSAGE_GOOD = '200 : OK'

# некорректные данные
USER_BAD = 'Lold'
RESPONSE_BAD = {variables.ERROR: 'Bad Request'}
MESSAGE_BAD = '400 : Bad Request'
EXPECTED_EXCEPTION = ValueError


class TestClass(unittest.TestCase):
    def test_process_answer_good(self):
        # Тест ответа сервера, статус 200
        self.assertEqual(server_process_answer(RESPONSE_GOOD), MESSAGE_GOOD)

    def test_process_answer_bad(self):
        # Тест ответа сервера, статус 400
        self.assertEqual(server_process_answer(RESPONSE_BAD), MESSAGE_BAD)

    def test_process_answer_error(self):
        # Тест исключение при ошибке от сервера
        self.assertRaises(EXPECTED_EXCEPTION, server_process_answer, RESPONSE_BAD)

    def test_create_presence_message_default(self):
        # Тест создания сообщения клиента
        message_main = {
            variables.ACTION: variables.PRESENCE,
            variables.TIME: TIME,
            variables.PORT: variables.DEFAULT_PORT,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_GOOD
            }
        }
        message = create_presence_msg()
        message[variables.TIME] = TIME
        self.assertEqual(message, message_main)


if __name__ == '__main__':
    unittest.main()