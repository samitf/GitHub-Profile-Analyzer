# src/analyze/api.py

import os
import requests
from typing import Optional, Dict, Any, List

GITHUB_API_URL = "https://api.github.com"

class GitHubAPI:
    def __init__(self, token: Optional[str] = None) -> None:
        """
        Initialize GitHub API wrapper.
        If no token is provided, it will try to read from environment variable GITHUB_TOKEN.
        """
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def _get(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        """
        Helper for GET requests with error handling.
        """
        url = f"{GITHUB_API_URL}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params or {})

        if response.status_code == 403:
            raise RuntimeError("GitHub API rate limit exceeded. Use a (GITHUB_TOKEN).")
        response.raise_for_status()
        return response.json()
    
    def get_user(self, username: str) -> Dict[str, Any]:
        """
        Fetch public profiles info of a user.
        """
        return self._get(f"/users/{username}")
    
    def get_repos(self, username: str) -> List[Dict[str, Any]]:
        """
        Fetch all public repositories of a user.
        """
        repos = []
        page = 1

        while True:
            data = self._get(f"/users/{username}/repos", params={"per_page": 100, "page": page})
            if not data:
                break
            repos.extend(data)
            page += 1
        return repos