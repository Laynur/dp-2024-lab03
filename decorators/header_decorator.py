from decorators.message_decorator import MessageDecorator
from interface.imessage import IMessage


class HeaderDecorator(MessageDecorator):
    """Класс декоратор для добавления заголовка к сообщению"""

    def __init__(self, text: IMessage, header: str):
        super().__init__(text)
        self._header = header

    def Print(self):
        """Метод для вывода сообщения"""
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения с добавлением заголовка"""
        return f"{self._header}\n{self._text.get_content()}"
