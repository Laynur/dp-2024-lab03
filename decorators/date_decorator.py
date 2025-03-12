from interface.imessage import IMessage
from decorators.message_decorator import MessageDecorator
from datetime import datetime


class DateDecorator(MessageDecorator):
    """Класс декоратор для добавления даты к сообщению"""

    def __init__(self, text: IMessage, date: str = None):
        super().__init__(text)
        self._date = date if date else datetime.now().strftime("%d.%m.%Y")

    def Print(self):
        """Метод для вывода сообщения"""
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения с добавлением даты"""
        return f"{self._text.get_content()}\n{self._date}"