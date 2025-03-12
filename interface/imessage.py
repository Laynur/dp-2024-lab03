from abc import ABC, abstractmethod


class IMessage(ABC):
    """Интерфейс сообщения"""

    @abstractmethod
    def Print(self):
        """Метод для вывода сообщения"""
        pass

    @abstractmethod
    def get_content(self):
        """Метод для возврата содержимого сообщения"""
        pass
