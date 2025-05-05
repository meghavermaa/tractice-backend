from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173"],
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
async def parse_repo(repo_link: str = Form(...)):
    print(f"Received repo link: {repo_link}")
    return {"message": f"Received repo link: {repo_link}"}

# uvicorn main:app --reload