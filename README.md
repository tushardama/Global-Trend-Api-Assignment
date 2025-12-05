# Simple TODO Viewer (JSONPlaceholder)

## Overview
This is a minimal Python script that fetches TODO items from the public JSONPlaceholder API.  
It supports two actions:
1. View all TODOs
2. View a TODO by its ID

The script also saves fetched data to a local cache file.

---

## Requirements
- Python 3
- requests library

Install dependency:
- pip install requests

---

## Features
- Fetches TODO data from:  
  https://jsonplaceholder.typicode.com/todos
- Saves data to `cache.json`
- Simple CLI with two options:
  - List all TODOs
  - Show details of a TODO by ID
- Basic error handling for network issues and invalid IDs

---

## Notes
- JSONPlaceholder returns mock test data.
- Cached data is overwritten each time the script runs.
