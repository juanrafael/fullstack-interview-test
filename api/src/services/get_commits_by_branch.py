from src.entities.branch import Branch
from src.repositories.commit_repository import CommitRepository

class GetCommitsByBranch:

    def __init__(self, repository: CommitRepository) -> None:
        self.repository = repository

    def execute(self, branch_name: str):
        branch = Branch(branch_name)
        if not self.exist_branch(branch):
            raise Exception(f"La rama {branch_name} no existe!")

        """print("Index: " + str(commit.Index))
        print("TYPES: " + str(commit.TYPES))
        print("author: " + str(commit.author))
        print("author_tz_offset: " + str(commit.author_tz_offset))
        print("authored_date: " + str(commit.authored_date))
        print("authored_datetime: " + str(commit.authored_datetime))
        print("binsha: " + str(commit.binsha))
        print("committed_date: " + str(commit.committed_date))
        print("committed_datetime: " + str(commit.committed_datetime))
        print("committer: " + str(commit.committer))
        print("committer_tz_offset: " + str(commit.committer_tz_offset))
        print("conf_encoding: " + str(commit.conf_encoding))
        print("count: " + str(commit.count))
        print("create_from_tree: " + str(commit.create_from_tree))
        print("data_stream: " + str(commit.data_stream))
        print("default_encoding: " + str(commit.default_encoding))
        print("diff: " + str(commit.diff))
        print("encoding: " + str(commit.encoding))
        print("env_author_date: " + str(commit.env_author_date))
        print("env_committer_date: " + str(commit.env_committer_date))
        print("gpgsig: " + str(commit.gpgsig))
        print("hexsha: " + str(commit.hexsha))
        print("iter_items: " + str(commit.iter_items))
        print("iter_parents: " + str(commit.iter_parents))
        print("list_items: " + str(commit.list_items))
        print("list_traverse: " + str(commit.list_traverse))
        print("message: " + str(commit.message))
        print("name_rev: " + str(commit.name_rev))
        print("new: " + str(commit.new))
        print("new_from_sha: " + str(commit.new_from_sha))
        print("parents: " + str(commit.parents))
        print("replace: " + str(commit.replace))
        print("repo: " + str(commit.repo))
        print("size: " + str(commit.size))
        print("stats: " + str(commit.stats))
        print("stream_data: " + str(commit.stream_data))
        print("summary: " + str(commit.summary))
        print("trailers: " + str(commit.trailers))
        print("traverse: " + str(commit.traverse))
        print("tree: " + str(commit.tree))
        print("type: " + str(commit.type))"""

        return self.repository.get_commits(branch)

    def exist_branch(self, branch_name: Branch):
        return self.repository.find_branch(branch_name)