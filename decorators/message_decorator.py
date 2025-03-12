from interface.imessage import IMessage


class MessageDecorator(IMessage):
    """Класс базового декоратора"""
    def __init__(self, text: IMessage):
        self._text = text

    def Print(self):
        """Метод для вывода сообщения"""
        print(self.get_content())

    def get_content(self) -> str:
        """Метод для возврата содержимого сообщения"""
        return self._text.get_content()