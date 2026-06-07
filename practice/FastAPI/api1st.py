from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

# uvicorn api1st:app --reload

app = FastAPI()

repository = {
    1 : {
        "readme" : "This repo contains files related to the project 1",
        "files" : ["app,py","requirements.txt","data.csv"],
        "owner" : "Pentayya"
    }
}

class Repo(BaseModel):
    readme: str
    files: list
    owner: str

class UpdateRepo(BaseModel):
    readme: Optional[str] = None
    files: Optional[list] = None
    owner: Optional[str] = None

#get
@app.get("/")
def home():
    return {"Namaste": "Ramyaa Baathula"}

#Path Parameter
@app.get("/get-repo/{repo_id}")
def get_repo(repo_id: int = Path(...,description="The ID of the repository you want to view",gt=0)):
    if repo_id in repository:
        return repository[repo_id]
    else:
        return {"error": "Repo not found"}
    
#Query Parameter
@app.get("/get-repo")
def get_repo(owner: Optional[str] = None):
    for repo_id in repository:
        if repository[repo_id]["owner"].lower() == owner.lower():
            return repository[repo_id]
        return {"error": "Repo not found for the given owner"}
    
#post
@app.post("/create-repo/{repo_id}")
def create_repo(repo_id: int, repo: Repo):
    if repo_id in repository:
        return {"error":"A repository already exists with this id"}
    repository[repo_id]= repo
    return {"Message":"Repository created sucessfully"},repository[repo_id]

#Put
@app.put("/update-repo/{repo_id}")
def update_repo(repo_id: int, repo: UpdateRepo):
    if repo_id not in repository:
        return {"error":"Repo not found"}
    if repo.readme is not None:
        repository[repo_id].readme = repo.readme
    if repo.files is not None:
        repository[repo_id].files = repo.files
    if repo.owner is not None:
        repository[repo_id].owner = repo.owner
    return {"Message":"Repository updated successfully"},repository[repo_id]

#delete
@app.delete("/delete-repo/{repo_id}")
def delete_repo(repo_id: int):
    if repo_id not in repository:
        return {"error":"Repo not found"}
    del repository[repo_id]
    return {"Message":"Repository deleted successfully"}