from src.entities.pull_request import PR
from config.connection import Connection

class PullRequestRepository(Connection):

    def __init__(self) -> None:
        super().__init__()

    def save_pull_request(self, pr: PR):
        sql = "INSERT INTO pull_requests (title, description, status, author, source_branch, target_branch, created_at) VALUES (%s, %s, %s,%s, %s, %s, %s)"
        self.exec(sql, (pr.title, pr.description, pr.status, pr.author, pr.source_branch, pr.target_branch, pr.created_at))
        self.commit()

    def get_all_pull_request(self):
        sql = "SELECT title, description, status, author, source_branch, target_branch, created_at FROM pull_requests"
        return self.get_all(sql)