class Branch(object):
    __name: str

    def __init__(self, name: str) -> None:
        self.__name = name

    def name(self) -> str:
        return self.__name

    def serialize(self):
        return {
            'name': self.name()
        }