from message import Message
from decorators.header_decorator import HeaderDecorator
from decorators.footer_decorator import FooterDecorator
from decorators.date_decorator import DateDecorator
from decorators.base_64_decorator import Base64Decorator

# msg = Message("Коллеги")
# msg.Print()
#
# msg = HeaderDecorator(Message("Коллеги"), "Добрый день!")
# msg.Print()
#
# msg = FooterDecorator(HeaderDecorator(Message("Коллеги"), "Добрый день!"), "С уважением")
# msg.Print()


msg = DateDecorator(FooterDecorator(HeaderDecorator(Message("Коллеги"), "Добрый день!"), "С уважением"))
msg.Print()

msg = Base64Decorator(DateDecorator(FooterDecorator(HeaderDecorator(Message("Коллеги"), "Добрый день!"), "С уважением")))
msg.Print()


