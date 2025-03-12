from decorators.message_decorator import MessageDecorator
from interface.imessage import IMessage


class FooterDecorator(MessageDecorator):
    """Класс декоратор для добавления подписи к сообщению"""
    def __init__(self, text: IMessage, footer: str):
        super().__init__(text)
        self._footer = footer

    def Print(self):
        """Метод для вывода сообщения"""
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения с добавлением подписи"""
        return f"{self._text.get_content()}\n{self._footer}"

