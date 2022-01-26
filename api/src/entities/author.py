class Author(object):
    __name: str
    __email: str

    def __init__(self, name: str, email: str) -> None:
        self.__name = name
        self.__email = email

    def name(self) -> str:
        return self.__name

    def email(self) -> str:
        return self.__email

    def serialize(self):
        return {
            "name": self.name(),
            "email": self.email(),
        }