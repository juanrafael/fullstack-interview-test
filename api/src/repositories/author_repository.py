from config.connection import Connection
from git import Repo
class AuthorRepository:
    def __init__(self, path) -> None:
        self.git = Repo(path, search_parent_directories=True)

    def get_author(self):
        pass