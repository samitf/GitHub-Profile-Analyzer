# src/tests/test_api.py

import pytest
import json
from unittest.mock import patch
from analyze.api import GitHubAPI

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
        self.headers = {}

    def json(self):
        return self._json

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise Exception(f"HTTP {self.status_code}")


def test_get_user_success():
    sample_user = {
        "login": "octocat",
        "id": 1,
        "name": "The Octocat",
        "public_repos": 2,
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = MockResponse(sample_user, 200)

        api = GitHubAPI(token=None)
        user = api.get_user("octocat")

        assert isinstance(user, dict)
        assert user["login"] == "octocat"
        assert user["name"] == "The Octocat"
        assert user["public_repos"] == 2

def test_get_repos_pagination():
    # simulate 2 pages: first with 2 repos, second empty
    repos_page_1 = [
        {"name": "repo1", "stargazers_count": 5},
        {"name": "repo2", "stargazers_count": 2},
    ]
    repos_page_2 = []

    # side_effect to return different responses per call
    def side_effect(url, headers=None, params=None):
        page = params.get("page", 1) if params else 1
        if page == 1:
            return MockResponse(repos_page_1, 200)
        else:
            return MockResponse(repos_page_2, 200)

    with patch("requests.get", side_effect=side_effect) as mock_get:
        api = GitHubAPI()
        repos = api.get_repos("octocat")

        assert isinstance(repos, list)
        assert len(repos) == 2
        assert repos[0]["name"] == "repo1"
        assert repos[1]["stargazers_count"] == 2

def test_rate_limit_raises_runtimeerror():
    # simulate 403 rate limit response for get_user
    with patch("requests.get") as mock_get:
        mock_get.return_value = MockResponse({"message": "rate limit"}, 403)

        api = GitHubAPI()
        with pytest.raises(RuntimeError):
            api.get_user("octocat")