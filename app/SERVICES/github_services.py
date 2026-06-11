import requests
from app.models.repo_models import RepoStructure

def get_repository(owner: str,repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch repository data: {response.status_code}")
    
    data = response.json()

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"]
    }

def get_repository_structure(owner: str,repo: str):
    
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch repository structure: {response.status_code}")
    
    data = response.json()

    folders=[]
    files=[]
    for item in data:
        if item["type"] == "dir":
            folders.append(item["name"])
        elif item["type"] == "file":
            files.append(item["name"])

    return RepoStructure(folders=folders,files=files)