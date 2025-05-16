import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def format_repo_name(repo):
    return repo.get("name", "").replace("-", " ").title()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Get list of all personal repos
def list_my_repos():
    url = "https://api.github.com/user/repos"
    params = {"per_page": 100, "type": "owner"}
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

# Get all branches for a repo
def get_branches(owner, repo_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/branches"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching branches for {repo_name}: {response.status_code}")
        return []

# Get commit count for a branch
def get_commit_count(owner, repo_name, branch_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    params = {"sha": branch_name, "per_page": 100}
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        commits = response.json()
        return len(commits)  # Note: Only up to 100
    else:
        print(f"Error fetching commits for {repo_name}/{branch_name}: {response.status_code}")
        return 0

# Main
if __name__ == "__main__":
    repos = list_my_repos()
    for repo in repos:
        repo_name = repo["name"]
        owner = repo["owner"]["login"]
        print(f"\n📘 Repository: {repo_name}")
        branches = get_branches(owner, repo_name)

        for branch in branches:
            branch_name = branch["name"]
            commit_count = get_commit_count(owner, repo_name, branch_name)
            print(f"  └─ 🌿 {branch_name}: {commit_count} commit(s)")
