"""Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id."""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/charlesnyanje"
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get(url, auth=(username, password))
    print(req.json().get('id'))
    