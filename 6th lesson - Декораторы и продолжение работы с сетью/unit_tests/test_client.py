import os, sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from lesson_6.client import server_process_answer
import lesson_6.common.variables as variables

ACTION_GOOD = variables.PRESENCE
USER_GOOD = 'Sergey'
TIME = 1.1
RESPONSE_GOOD = {variables.RESPONSE: 200}
PORT = variables.DEFAULT_PORT
MESSAGE_GOOD = '200 : OK'

USER_BAD = 'Lold'
MESSAGE_BAD = '400 : Bad Request'
RESPONSE_BAD = {variables.ERROR: 'Bad Request'}
EXPECTED_EXCEPTION = ValueError


class TestClass(unittest.TestCase):

    def test_process_answer_good(self):
        #   Тест ответа сервера, статус 200
        self.assertEqual(server_process_answer(RESPONSE_GOOD), MESSAGE_GOOD)

    def test_process_answer_bad(self):
        #   Тест ответа сервера, статус 400
        self.assertEqual(server_process_answer(RESPONSE_BAD), MESSAGE_BAD)

    def test_process_answer_error(self):
        #   Тест исключение при ошибке от сервера
        self.assertRaises(EXPECTED_EXCEPTION, server_process_answer, RESPONSE_BAD)


if __name__ == '__main__':
    unittest.main()