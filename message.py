from interface.imessage import IMessage


class Message(IMessage):
    """Класс базового сообщения"""

    def __init__(self, text: str):
        self.text = text

    def Print(self):
        print(self.text)