from fastapi import APIRouter
from app.SERVICES.github_services import get_repository

router = APIRouter()

@router.get("/get-repo")
def get_repo(owner: str,repo: str):
    return get_repository(owner,repo)
