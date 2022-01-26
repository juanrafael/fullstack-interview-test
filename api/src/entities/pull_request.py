from .author import Author
class PR:

    __title: str
    __description: str
    __status: str
    __author: Author

    def __init__(self, title, description, status, author: Author) -> None:
        self.__title = title
        self.__description = description
        self.__status = status
        self.__author = author