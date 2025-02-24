from interface.imessage import IMessage


class Message(IMessage):
    """Класс базового сообщения"""

    def __init__(self, text: str):
        self._text = text

    def Print(self):
        """Метод для вывода сообщения"""
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения"""
        return self._text
