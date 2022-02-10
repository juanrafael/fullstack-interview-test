from git import Repo
from src.entities.author import Author
from config.connection import Connection

class AuthorRepository(Connection):
    def __init__(self) -> None:
        super().__init__()

    def save_author(self, name, email):
        repositorio = None

    def get_authors(self):
        sql = "SELECT * FROM authors;"
        return self.get_all(sql)