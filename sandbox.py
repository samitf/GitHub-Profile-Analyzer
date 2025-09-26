# sandbox.py

import sys
import os
import json
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

try:
    from analyze.api import GitHubAPI
    from analyze.analyzer import analyze_repos
except Exception as e:
    raise SystemExit(f"Import error: {e}\nMake sure src/analyze/__init__.py exists and paths are correct.")

def run(username: str, save_json: bool = False, out_path: str | None = None):
    token = os.getenv("GITHUB_TOKEN")
    client = GitHubAPI(token=token)
    print(f"Fetching repos for '{username}' (token set: {bool(token)})...")
    repos = client.get_repos(username)
    print(f"Fetched {len(repos)} repos. Running analysis...")
    result = analyze_repos(username, repos, top_n=10)

    try:
        data = result.to_dict() if hasattr(result, "to_dict") else result.__dict__
    except Exception:
        data = result.__dict__ if hasattr(result, "__dict__") else str(result)

    print(json.dumps(data, indent=2, ensure_ascii=False))

    if save_json:
        out = out_path or f"{username}_analysis.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved analysis JSON to: {out}")

if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Quick sandbox runner for GitHub analyzer")
    p.add_argument("username", help="GitHub username to analyze")
    p.add_argument("--save", action="store_true", help="Save JSON output to a file")
    p.add_argument("--out", help="Output filename (if --save used). Default: <username>_analysis.json")
    args = p.parse_args()

    run(args.username, save_json=args.save, out_path=args.out)
