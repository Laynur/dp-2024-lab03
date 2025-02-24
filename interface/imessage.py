from abc import ABC, abstractmethod


class IMessage(ABC):
    """Интерфейс сообщения"""

    @abstractmethod
    def Print(self):
        """метод для вывода сообщения"""
        pass