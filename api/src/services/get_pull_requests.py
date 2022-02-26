from src.repositories.pull_request_repository import PullRequestRepository
from src.entities.pull_request import PR

class GetPullRequests:

    def __init__(self, repository: PullRequestRepository) -> None:
        self.repository = repository

    def execute(self):
        get_prs = self.repository.get_all_pull_request()
        if len(get_prs) == 0:
            raise Exception('Aun no hay ningun pull request creado!')

        return [PR(pr[0], pr[1], pr[2], pr[3], pr[4], pr[5], pr[6]).serialize() for pr in get_prs]