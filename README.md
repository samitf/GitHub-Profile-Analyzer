# GitHub Profile Analyzer

A Python project to analyze public GitHub profiles using the GitHub API.  
Currently, it supports fetching repositories of a given user and generating useful insights such as:

---

- 📦 Total repositories  
- ⭐ Total stars & average stars per repo  
- 🍴 Total forks  
- 🏆 Top repositories by stars  
- 🧑‍💻 Language distribution  
- 📅 Activity timeline by year  

---

## 🚀 Features (In Progress...⏳⌛)
- Lightweight GitHub API wrapper (`api.py`)  
- Analyzer module (`analyzer.py`) for extracting metrics from repo data  
- Sandbox script (`sandbox.py`) to quickly fetch + analyze + view JSON results  
- Extensible design for future CLI, visualization, and HTML report generation  

---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/github-profile-analyzer.git
   cd github-profile-analyzer

2. **Create and activate a virtual environment**
   ```bash
   # macOS / Linux
   python -m venv .venv
   source .venv/bin/activate
   ```
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt

---

## ▶️ Usage
```bash
# Basic usage
python sandbox.py [username]
```
Example: ```python sandbox.py samitf```
```bash
# Save JSON output to <username>_analysis.json
python sandbox.py [username] --save
```
Example: ```python sandbox.py samitf --save```
```bash
# Save JSON with a custom filename
python sandbox.py [username] --save --out report.json
```
Example: ```python sandbox.py samitf --save --out report.json```

---

## ➡️Output Example
- ```python sandbox.py samitf```
- Output:
  ```
  Fetching repos for 'samitf' (token set: False)...
  Fetched 17 repos. Running analysis...
  ```
- Output JSON:
  ```JSON
  {
    "username": "samitf",
    "total_repos": 17,
    "total_stars": 5,
    "total_forks": 5,
    "avg_stars_per_repo": 0.29,
    "top_repos_by_stars": [
      {
        "name": "Legal-Case-Summarization",
        "stars": 2,
        "forks": 2,
        "language": "Jupyter Notebook",
        "size_kb": 5929,
        "html_url": "https://github.com/samitf/Legal-Case-Summarization",
        "created_at": "2025-05-01T10:33:55+00:00",
        "pushed_at": "2025-05-01T11:46:15+00:00"
      },
      {
        "name": "My-Projects",
        "stars": 1,
        "forks": 1,
        "language": "Jupyter Notebook",
        "size_kb": 12766,
        "html_url": "https://github.com/samitf/My-Projects",
        "created_at": "2024-06-25T11:15:11+00:00",
        "pushed_at": "2025-01-06T13:15:06+00:00"
      },
      {
        "name": "Portfolio",
        "stars": 1,
        "forks": 0,
        "language": "CSS",
        "size_kb": 21770,
        "html_url": "https://github.com/samitf/Portfolio",
        "created_at": "2025-06-23T07:42:49+00:00",
        "pushed_at": "2025-07-01T15:03:48+00:00"
      },
      {
        "name": "ResumAI",
        "stars": 1,
        "forks": 0,
        "language": "Python",
        "size_kb": 266,
        "html_url": "https://github.com/samitf/ResumAI",
        "created_at": "2025-06-13T16:05:05+00:00",
        "pushed_at": "2025-06-13T16:27:19+00:00"
      },
      {
        "name": "BabyLLM",
        "stars": 0,
        "forks": 0,
        "language": "Python",
        "size_kb": 28,
        "html_url": "https://github.com/samitf/BabyLLM",
        "created_at": "2025-07-16T16:37:23+00:00",
        "pushed_at": "2025-07-16T18:13:51+00:00"
      },
      {
        "name": "DeepFake-Detection-React-Website",
        "stars": 0,
        "forks": 1,
        "language": "JavaScript",
        "size_kb": 1481,
        "html_url": "https://github.com/samitf/DeepFake-Detection-React-Website",
        "created_at": "2024-04-01T13:15:07+00:00",
        "pushed_at": "2024-06-24T10:12:17+00:00"
      },
      {
        "name": "Email-Spam-Filter-SVM",
        "stars": 0,
        "forks": 1,
        "language": "HTML",
        "size_kb": 247,
        "html_url": "https://github.com/samitf/Email-Spam-Filter-SVM",
        "created_at": "2023-04-29T14:46:45+00:00",
        "pushed_at": "2023-07-20T04:26:44+00:00"
      },
      {
        "name": "Financial-Email-Assistant",
        "stars": 0,
        "forks": 0,
        "language": "HTML",
        "size_kb": 218,
        "html_url": "https://github.com/samitf/Financial-Email-Assistant",
        "created_at": "2025-07-04T10:31:50+00:00",
        "pushed_at": "2025-07-04T10:45:08+00:00"
      },
      {
        "name": "frontend-BabyLLM",
        "stars": 0,
        "forks": 0,
        "language": "HTML",
        "size_kb": 1901,
        "html_url": "https://github.com/samitf/frontend-BabyLLM",
        "created_at": "2025-07-16T18:22:43+00:00",
        "pushed_at": "2025-07-16T18:24:40+00:00"
      },
      {
        "name": "GitHub-Profile-Analyzer",
        "stars": 0,
        "forks": 0,
        "language": "Python",
        "size_kb": 5,
        "html_url": "https://github.com/samitf/GitHub-Profile-Analyzer",
        "created_at": "2025-09-24T16:14:59+00:00",
        "pushed_at": "2025-09-26T16:35:08+00:00"
      }
    ],
    "language_counts": {
      "Python": 4,
      "JavaScript": 1,
      "HTML": 5,
      "Jupyter Notebook": 4,
      "CSS": 1,
      "Unknown": 2
    },
    "activity_by_year": {
      "2023": 2,
      "2024": 1,
      "2025": 14
    }
  }
  ```
