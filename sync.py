import os
import requests

# সোর্স ফাইলের Raw URL (যেটি আপনি স্ক্র্যাপ/কপি করতে চান)
SOURCE_URL = "https://raw.githubusercontent.com/drmlive/sliv-live-events/main/sonyliv.json"
TARGET_FILE = "sonyliv.json"

def fetch_and_save():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(SOURCE_URL, headers=headers)
    
    if response.status_code == 200:
        with open(TARGET_FILE, "wb") as f:
            f.write(response.content)
        print(f"Successfully synced {TARGET_FILE}")
    else:
        print(f"Failed to fetch data: HTTP {response.status_code}")

if __name__ == "__main__":
    fetch_and_save()
