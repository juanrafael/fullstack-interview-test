class File(object):
    __name: str
    __type: str
    __blob: str

    def __init__(self, name, type, blob) -> None:
        self.__name = name
        self.__type = type
        self.__blob = blob

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_blob(self):
        return self.__blob

    def serialize(self):
        return {
            "name": self.get_name(),
            "type": self.get_type(),
            "blob": self.get_blob(),
        }