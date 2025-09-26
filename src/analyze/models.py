# src/analyze/models.py

from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List, Optional

@dataclass
class RepoSummary:
    name: str
    stars: int
    forks: int
    language: Optional[str]
    size_kb: int
    created_at: Optional[datetime]
    pushed_at: Optional[datetime]
    html_url: Optional[str]

    @classmethod
    def from_api(cls, repo_json: Dict) -> "RepoSummary":
        def parse_dt(s):
            return datetime.fromisoformat(s.replace("Z","+00:00")) if s else None
        
        return cls(
            name = repo_json.get("name"),
            stars = repo_json.get("stargazers_count", 0),
            forks = repo_json.get("forks_count", 0),
            language = repo_json.get("language"),
            size_kb = repo_json.get("size", 0),
            created_at = parse_dt(repo_json.get("created_at")),
            pushed_at = parse_dt(repo_json.get("pushed_at")),
            html_url = repo_json.get("html_url"),
        )
    
    
@dataclass
class AnalysisResult:
    username: str
    total_repos: int
    total_stars: int
    total_forks: int
    avg_stars_per_repo: float
    top_repos_by_stars: List[RepoSummary]
    language_counts: Dict[Optional[str], int]
    activity_by_year: Dict[int, int]

    def to_dict(self):
        d = asdict(self)
        # converting RepoSummary dataclasses to dicts
        d["top_repos_by_stars"] = [
            {
                **{k: v for k, v in r.__dict__.items() if not isinstance(v, datetime)},
                "created_at": r.created_at.isoformat() if r.created_at else None,
                "pushed_at": r.pushed_at.isoformat() if r.pushed_at else None,
            }
            for r in self.top_repos_by_stars
        ]
        return d