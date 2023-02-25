import requests

import os

import time

# GitHub repository information

owner = "tanmayd004"

repo = "client-file-auto-update"

filename = "client.py"

# GitHub API endpoint for getting the latest commit timestamp

endpoint = f"https://api.github.com/tanmayd004/client-file-auto-update/commits?path=client.py&per_page=1"

def check_for_updates():

    try:

        # Send a GET request to the GitHub API endpoint

        response = requests.get(endpoint)

        # Raise an exception if the request failed

        response.raise_for_status()

        # Parse the response JSON to get the last commit timestamp

        commit = response.json()[0]

        server_version = commit['commit']['committer']['date']

        # Convert the timestamp to a float

        server_version = time.mktime(time.strptime(server_version, '%Y-%m-%dT%H:%M:%SZ'))

        # Compare the server version with the local version

        client_version = os.path.getmtime(filename)

        if server_version > client_version:

            print('New version available. Updating...')

            update()

    except Exception as e:

        print(f"Error: {e}")

        print("Failed to check for updates.")

def update():

    try:

        # Download the latest file from GitHub

        response = requests.get(f"https://raw.githubusercontent.com/tanmayd004/client-file-auto-udate/client.py")

        # Raise an exception if the request failed

        response.raise_for_status()

        with open(filename, "wb") as f:

            f.write(response.content)

        print(f"{filename} updated successfully!")

    except Exception as e:

        print(f"Error: {e}")

        print("Failed to update the file.")

# Check for updates every minute

while True:

    check_for_updates()

    time.sleep(60)

