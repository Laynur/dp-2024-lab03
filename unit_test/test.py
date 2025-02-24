import unittest

from message import Message


class TestDecorators(unittest.TestCase):
    """Тест-кейсы для проверки декораторов"""

    def test_message(self):
        """Кейс: проверка класса Message. Проверка на возврат корректного значения"""
        msg = Message("Привет")
        test_text = "Привет"
        self.assertEqual(msg.get_content(), test_text)
