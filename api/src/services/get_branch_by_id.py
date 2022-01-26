from src.repositories.branch_repository import BranchRepository

class GetBranchById:

    def __init__(self, repository: BranchRepository, id) -> None:
        self.repository = repository
        self.id = id

    def execute(self):
        return self.repository.get_branches()