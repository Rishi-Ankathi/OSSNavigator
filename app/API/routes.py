from fastapi import APIRouter
from app.services.github_services import get_repository,get_repository_structure


router = APIRouter()

@router.get("/get-repo")
def get_repo(owner: str,repo: str):
    return get_repository(owner,repo)

@router.get("/get-repo-structure")
def get_repo_structure(owner: str, repo: str):
    return get_repository_structure(owner, repo)