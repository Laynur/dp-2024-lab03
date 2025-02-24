from message import Message
from decorators.header_decorator import HeaderDecorator
from decorators.footer_decorator import FooterDecorator
from decorators.date_decorator import DateDecorator
from decorators.base_64_decorator import Base64Decorator
# msg = Message("Пора идти на пересдачу")
# msg.Print()
#
# msg = HeaderDecorator(Message("Пора идти на пересдачу"), "Дорогой мой друг!")
# msg.Print()
#
# msg = FooterDecorator(HeaderDecorator(Message("Пора идти на пересдачу"), "Дорогой мой друг!"), "Твой брат")
# msg.Print()


# msg = DateDecorator(FooterDecorator(HeaderDecorator(Message("Пора идти на пересдачу"), "Дорогой мой друг!"), "Твой брат"))
# msg.Print()

msg = Base64Decorator(DateDecorator(FooterDecorator(HeaderDecorator(Message("Пора идти на пересдачу"), "Дорогой мой друг!"), "Твой брат")))
msg.Print()


