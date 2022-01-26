from datetime import datetime
from .file import File
from .author import Author

class Commit(object):
    __hexsha: str
    __author: Author
    __message: str
    __date: datetime

    def __init__(self, hexsha: str, author: Author, date, message: str) -> None:
        self.__hexsha = hexsha
        self.__author = author
        #self.__date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__date = date
        self.write_a_message(message)

    def get_hexsha(self) -> str:
        return self.__hexsha

    def write_a_message(self, message: str) -> None:
        self.__message = message

    def get_message(self) -> str:
        return self.__message

    def get_author(self) -> Author:
        return self.__author

    def get_date(self) -> datetime:
        return self.__date

    def serialize(self):
        return {
            "hexsha": self.get_hexsha(),
            "author": self.get_author().serialize(),
            "message": self.get_message(),
            "datetime": self.get_date(),
        }

class ChangesCommit(object):
    __number_file_changed: int
    __additions: int
    __deletions: int
    __files: list

    def __init__(self, number_file_changed, additions, deletions, files) -> None:
        self.__number_file_changed = number_file_changed
        self.__additions = additions
        self.__deletions = deletions
        self.__files = files

    def get_number_file_changed(self):
        return self.__number_file_changed

    def get_additions(self):
        return self.__additions

    def get_deletions(self):
        return self.__deletions

    def get_files(self):
        return self.__files

    def serialize(self):
        return {
            "number_file_changed": self.get_number_file_changed(),
            "additions": self.get_additions(),
            "deletions": self.get_deletions(),
            "files": self.get_files(),
        }