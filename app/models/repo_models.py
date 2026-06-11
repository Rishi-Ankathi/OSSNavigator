from pydantic import BaseModel

class RepoStructure(BaseModel):
    folders: list
    files: list