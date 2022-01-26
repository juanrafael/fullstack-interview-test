from src.repositories.branch_repository import BranchRepository

class GetBranches:

    def __init__(self, repository: BranchRepository) -> None:
        self.repository = repository

    def execute(self):
        return self.repository.get_branches()