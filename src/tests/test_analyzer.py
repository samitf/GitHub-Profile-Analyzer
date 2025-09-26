# src/tests/test_analyzer.py

from datetime import datetime
from analyze.analyzer import analyze_repos
from analyze.models import RepoSummary

SAMPLE_REPOS = [
    {
        "name": "repo1",
        "stargazers_count": 10,
        "forks_count": 2,
        "language": "Python",
        "size": 123,
        "created_at": "2020-01-01T00:00:00Z",
        "pushed_at": "2021-06-01T00:00:00Z",
        "html_url": "https://github.com/u/repo1",
    },
    {
        "name": "repo2",
        "stargazers_count": 5,
        "forks_count": 1,
        "language": "JavaScript",
        "size": 200,
        "created_at": "2019-03-01T00:00:00Z",
        "pushed_at": "2023-01-01T00:00:00Z",
        "html_url": "https://github.com/u/repo2",
    },
]

def test_analyze_repos_basic():
    result = analyze_repos("octocat", SAMPLE_REPOS, top_n=2)
    assert result.username == "octocat"
    assert result.total_repos == 2
    assert result.total_stars == 15
    assert result.total_forks == 3
    assert result.avg_stars_per_repo == 7.5
    assert isinstance(result.top_repos_by_stars[0], RepoSummary)
    assert "Python" in result.language_counts
    assert isinstance(result.activity_by_year, dict)