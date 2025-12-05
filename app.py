import requests
import json
import os

API = "https://jsonplaceholder.typicode.com/todos"
CACHE = "cache.json"

def fetch_todos():
    try:
        r = requests.get(API, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error fetching data:", e)
        return []

def load_cache():
    if os.path.exists(CACHE):
        try:
            with open(CACHE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_cache(data):
    with open(CACHE, "w") as f:
        json.dump(data, f, indent=2)

def main():
    todos = fetch_todos()
    save_cache(todos)

    print("1 = View all TODOs")
    print("2 = View TODO by ID")

    choice = input("Option: ")

    if choice == "1":
        print(json.dumps(todos, indent=2))

    elif choice == "2":
        try:
            tid = int(input("Enter ID: "))
        except:
            print("Invalid ID")
            return

        item = next((t for t in todos if t.get("id") == tid), None)
        print(json.dumps(item, indent=2) if item else "Not found")

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()