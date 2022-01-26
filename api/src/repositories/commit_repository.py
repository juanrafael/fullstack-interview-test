from src.entities.author import Author
from src.entities.branch import Branch
from src.entities.commit import Commit, ChangesCommit
from src.entities.file import File
from git import Repo

class CommitRepository:

    def __init__(self, path) -> None:
        self.git = Repo(path, search_parent_directories=True)

    def get_commits(self, branch: Branch):
        branch_id = 'origin/' + branch.name()
        commits = list(self.git.iter_commits(branch_id))
        return [Commit(commit.hexsha, Author(commit.author.name, commit.author.email), commit.committed_datetime, commit.message).serialize() for commit in commits]

    def find_branch(self, branch_name: Branch):
        branches = self.git.remote().refs
        for branch in branches:
            if branch.name.split('/')[-1] == branch_name.name():
                return True
        return False

    def get_commit(self, hexsha: str):
        commit = self.git.commit(hexsha)
        get_commit = Commit(commit.hexsha, Author(commit.author.name, commit.author.email), commit.committed_datetime, commit.message).serialize()
        return self.get_files_changed(commit, get_commit)

    def get_files_changed(self, commit, commit_dict: dict):
        files = [File(file.b_blob.name, file.b_blob.type, file.b_blob.data_stream.read().decode('utf-8')).serialize() for file in commit.diff('HEAD~1').iter_change_type('M')]
        #print([dir(blob) for blob in commit.stats])
        print(commit.stats.files)
        print(commit.stats.total)

        for diff in commit.diff('HEAD~1'):
            print('######## ##########')
            print(diff.change_type)
            print(f"{diff.a_path} -> {diff.b_path}")


        commit_dict['files_changed'] = ChangesCommit(commit.stats.total['files'], commit.stats.total['insertions'], commit.stats.total['deletions'], files).serialize()

        return commit_dict