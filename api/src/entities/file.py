class File(object):
    __name: str

    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name

    def serialize(self):
        return {
            "name": self.get_name()
        }