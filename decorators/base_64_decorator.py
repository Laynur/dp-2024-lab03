import base64
from decorators.message_decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    """Класс декоратор для кодирования содержимого сообщения в Base64 формат"""

    def Print(self):
        """Метод для вывода сообщения """
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения в формате Base64"""
        return base64.b64encode(self._text.get_content().encode("utf-8")).decode("utf-8")
