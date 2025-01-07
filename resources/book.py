from dataclasses import dataclass


@dataclass
class Books:
    name: str
    author: str
    quantity: str


book = Books(name="Гарри Поттер и философский камень", author="Джоан Кэтлин Роулинг", quantity="1")
