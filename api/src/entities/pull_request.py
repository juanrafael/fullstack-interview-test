from datetime import datetime
class PR(object):

    title: str
    description: str
    status: str
    author: str
    source_branch: str
    target_branch: str
    created_at: datetime

    def __init__(self, title, description, status, author, source_branch, target_branch, created_at) -> None:
        self.set_title(title)
        self.set_description(description)
        self.status = status
        self.author = author
        self.set_source_branch(source_branch)
        self.set_target_branch(target_branch)
        self.created_at = created_at

    def set_title(self, title):
        if not title or len(title) == 0:
            raise Exception("el titulo es obligatorio!")

        self.title = title


    def set_description(self, description):
        if not description or len(description) == 0:
            raise Exception("La descripción del PR es obligatoria!")

        self.description = description


    def set_source_branch(self, source_branch):
        if not source_branch or len(source_branch) == 0:
            raise Exception("La rama origen es obligatoria!")

        self.source_branch = source_branch


    def set_target_branch(self, target_branch):
        if not target_branch or len(target_branch) == 0:
            raise Exception("La rama destino es obligatoria!")

        self.target_branch = target_branch


    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "author": self.author,
            "source_branch": self.source_branch,
            "target_branch": self.target_branch,
            "created_at": self.created_at.strftime('%B %d, %Y %H:%M:%S')
        }