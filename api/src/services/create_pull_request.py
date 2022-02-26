from datetime import datetime
from src.repositories.pull_request_repository import PullRequestRepository
from src.entities.pull_request import PR

class CreatePullRequest:

    def __init__(self, repository: PullRequestRepository) -> None:
        self.repository = repository

    def execute(self, data):
        pull_request = PR(data['title'], data['description'], 'open', 'alejandro rafael chavez', data['branch_source'], data['branch_target'], datetime.now())
        self.repository.save_pull_request(pull_request)