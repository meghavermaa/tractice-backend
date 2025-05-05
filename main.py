from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173"],  # frontend dev URL
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

GITHUB_API = "https://api.github.com/repos"

class RepoRequest(BaseModel):
  repo_url: str

@app.get("/")
def read_root():
  return {"message": "Backend is working!"}

@app.post("/parse-repo")
def parse_repo(req: RepoRequest):
  return {"message": f"Received repo URL: {req.repo_url}"}

# uvicorn main:app --reload