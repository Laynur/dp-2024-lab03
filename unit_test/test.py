import base64
import unittest
from datetime import datetime

from message import Message
from decorators.header_decorator import HeaderDecorator
from decorators.footer_decorator import FooterDecorator
from decorators.date_decorator import DateDecorator
from decorators.base_64_decorator import Base64Decorator


class TestDecorators(unittest.TestCase):
    """Тест-кейсы для проверки декораторов"""

    def test_message(self):
        """Кейс: проверка Message. Проверка на возврат корректного значения"""
        msg = Message("Привет")
        test_text = "Привет"
        self.assertEqual(msg.get_content(), test_text)

    def test_header_decorator(self):
        """Кейс: проверка HeaderDecorator. Проверка добавления заголовка к сообщению"""
        msg = HeaderDecorator(Message("Коллеги"), "Добрый день!")
        test_text = "Добрый день!\nКоллеги"
        self.assertEqual(msg.get_content(), test_text)

    def test_footer_decorator(self):
        """Кейс: проверка FooterDecorator. Проверка добавления подписи к сообщению"""
        msg = FooterDecorator(Message("Коллеги"),"С уважением")
        test_text = "Коллеги\nС уважением"
        self.assertEqual(msg.get_content(), test_text)

    def test_date_decorator(self):
        """Кейс: проверка DateDecorator. Проверка добавления добавления указанной даты к сообщению"""
        msg = DateDecorator(Message("Коллеги"),"22.05.2001")
        test_text = "Коллеги\n22.05.2001"
        self.assertEqual(msg.get_content(),test_text)

    def test_date_decorator_current_date(self):
        """Кейс: проверка DateDecorator. Проверка добавления добавления текущей даты к сообщению"""
        msg = DateDecorator(Message("Коллеги"))
        test_text = f"Коллеги\n{datetime.now().strftime("%d.%m.%Y")}"
        self.assertEqual(msg.get_content(), test_text)

    def test_base64_decorator(self):
        """Кейс: проверка Base64Decorator. Проверка кодирования содержимого сообщения в формате Base64"""
        msg = Base64Decorator(Message("Коллеги"))
        test_text = base64.b64encode("Коллеги".encode("utf-8")).decode("utf-8")
        self.assertEqual(msg.get_content(), test_text)

    def test_all_decorators(self):
        """Кейс: проверка работы всех декораторов"""
        msg = Base64Decorator(DateDecorator(
            FooterDecorator(HeaderDecorator(Message("Коллеги"), "Добрый день!"), "С уважением")))
        test_text = f"Добрый день!\nКоллеги\nС уважением\n{datetime.now().strftime("%d.%m.%Y")}"
        encode_text = base64.b64encode(test_text.encode("utf-8")).decode(
            "utf-8"
        )
        self.assertEqual(msg.get_content(),encode_text)