# src/analyze/analyzer.py

from collections import Counter, defaultdict
from typing import List, Dict
from datetime import datetime

from .models import RepoSummary, AnalysisResult

def build_repo_summaries(repos_json: List[Dict]) -> List[RepoSummary]:
    """Convert list of GitHub repo JSON objects to RepoSummary dataclasses."""
    return [RepoSummary.from_api(r) for r in repos_json]

def analyze_repos(username: str, repos_json: List[Dict], top_n: int = 5) -> AnalysisResult:
    repos = build_repo_summaries(repos_json)
    total_repos = len(repos)
    total_stars = sum(r.stars for r in repos)
    total_forks = sum(r.forks for r in repos)
    avg_stars = (total_stars / total_repos) if total_repos else 0.0

    # top repos by stars
    top_repos = sorted(repos, key=lambda r: r.stars, reverse=True)[:top_n]

    # language distribution
    lang_counter = Counter((r.language or "Unknown") for r in repos)

    # activity by year
    activity = defaultdict(int)
    for r in repos:
        dt = r.pushed_at or r.created_at
        if dt:
            activity[dt.year] += 1

    # sort activity by year and convert to normal dict
    activity_by_year = dict(sorted(activity.items()))

    return AnalysisResult(
        username=username,
        total_repos=total_repos,
        total_stars=total_stars,
        total_forks=total_forks,
        avg_stars_per_repo=round(avg_stars, 2),
        top_repos_by_stars=top_repos,
        language_counts=dict(lang_counter),
        activity_by_year=activity_by_year,
    )