from src.repositories.commit_repository import CommitRepository

class GetCommitByHexsha:

    def __init__(self, repository: CommitRepository) -> None:
        self.repository = repository

    def execute(self, commit_hexsha: str):
        commit = self.repository.get_commit(commit_hexsha)
        return commit