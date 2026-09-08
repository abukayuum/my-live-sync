import os
import requests

FILES_TO_SYNC = [
    {
        "source": "https://raw.githubusercontent.com/drmlive/sliv-live-events/main/sonyliv.json",
        "target": "sonyliv.json"
    },
    {
        "source": "https://raw.githubusercontent.com/drmlive/sliv-live-events/main/sonyliv.m3u",
        "target": "sonyliv.m3u"
    }
]

def fetch_files():
    headers = {"User-Agent": "Mozilla/5.0"}
    for item in FILES_TO_SYNC:
        try:
            res = requests.get(item["source"], headers=headers, timeout=15)
            if res.status_code == 200:
                with open(item["target"], "wb") as f:
                    f.write(res.content)
                print(f"Synced {item['target']}")
            else:
                print(f"Failed to fetch {item['target']}: HTTP {res.status_code}")
        except Exception as e:
            print(f"Error fetching {item['target']}: {e}")

def get_source_commit_info():
    api_url = "https://api.github.com/repos/drmlive/sliv-live-events/commits/main"
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(api_url, headers=headers, timeout=10)
        if res.status_code == 200:
            commit_data = res.json()
            source_time = commit_data["commit"]["committer"]["date"]
            source_sha = commit_data["sha"][:7]
            
            if "GITHUB_ENV" in os.environ:
                with open(os.environ["GITHUB_ENV"], "a") as env_file:
                    env_file.write(f"SOURCE_COMMIT_TIME={source_time}\n")
                    env_file.write(f"SOURCE_SHA={source_sha}\n")
    except Exception as e:
        print(f"Error fetching commit info: {e}")

if __name__ == "__main__":
    fetch_files()
    get_source_commit_info()
