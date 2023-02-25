import requests

import os

# GitHub repository information

owner = "tanmayd004"

repo = "client-file-auto-update"

filename = "client.py"

# GitHub API endpoint for getting the latest commit information

endpoint = f"https://api.github.com/tanmayd004/client-file-auto-update/commits?path=client.py&per_page=1"

def check_for_updates():

    # Send a GET request to the GitHub API endpoint

    response = requests.get(endpoint)

    # Parse the response JSON to get the last commit timestamp

    commit = response.json()[0]

    server_version = commit['commit']['committer']['date']

    # Convert the timestamp to a float

    server_version = float(server_version)

    # Compare the server version with the local version

    client_version = os.path.getmtime(filename)

    if server_version > client_version:

        print('New version available. Updating...')

        update()

def update():

    # Download the latest file from GitHub

    response = requests.get(f"https://raw.githubusercontent.com/{owner}/{repo}/main/{filename}")

    with open(filename, "wb") as f:

        f.write(response.content)

    print(f"{filename} updated successfully!")

# Check for updates every minute

while True:

    check_for_updates()

    time.sleep(60)

