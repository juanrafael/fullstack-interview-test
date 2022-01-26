from git import Repo
from src.entities.branch import Branch

class BranchRepository:

    def __init__(self, path) -> None:
        self.git = Repo(path, search_parent_directories=True)

    def get_branches(self):
        branches = self.git.remote().refs
        return [Branch(branch.name.split('/')[-1]).serialize() for branch in branches]