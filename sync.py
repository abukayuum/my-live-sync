import os
import requests

# যে যে ফাইল আপনি সোর্স থেকে কপি করতে চান
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

def fetch_and_save():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    for item in FILES_TO_SYNC:
        url = item["source"]
        target = item["target"]
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                with open(target, "wb") as f:
                    f.write(response.content)
                print(f"Successfully synced: {target}")
            else:
                print(f"Failed to fetch {target}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error fetching {target}: {e}")

if __name__ == "__main__":
    fetch_and_save()
