"""REST API starter. Students should extend validation and metadata capture."""

import requests
import json
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUT_PATH = Path("data/raw/api_snapshot.json")

def fetch_records():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    print(f"Status Code: {response.status_code}")
    return response.json()

if __name__ == "__main__":
    records = fetch_records()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(records, f, indent=2)
    print(f"API data saved to {OUT_PATH}")