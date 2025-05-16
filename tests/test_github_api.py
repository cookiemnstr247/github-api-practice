import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import get_branches

def test_get_branches_returns_list():
    owner = "cookiemnstr247"
    repo = "datasharing"

    branches = get_branches(owner, repo)

    assert isinstance(branches, list)
    assert len(branches) > 0
    assert "name" in branches[0]


def test_format_repo_name():
    repo = {"name": "github-api-practice"}
    assert format_repo_name(repo) == "Github Api Practice"