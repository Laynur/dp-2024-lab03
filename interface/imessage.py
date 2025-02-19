from abc import ABC, abstractmethod


class IMessage(ABC):
    """Интерфейс сообщения"""

    @abstractmethod
    def print(self):
        """метод для вывода сообщения"""
        pass