import requests
import os
import sys
import subprocess

def get_latest_version(url):
    """Fetches the latest version number from a remote server."""
    try:
        response = requests.get(url)
        return response.text.strip()
    except requests.RequestException:
        return None

def download_update(update_url, filename="update.zip"):
    """Downloads the update file from the given URL."""
    try:
        response = requests.get(update_url, stream=True)
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filename
    except requests.RequestException:
        return None

def restart_program():
    """Restarts the program after an update."""
    python = sys.executable
    os.execl(python, python, *sys.argv)

def check_and_update(current_version, version_url, update_url):
    """Checks for an update and applies it if available."""
    latest_version = get_latest_version(version_url)
    if latest_version and latest_version > current_version:
        print(f"New version {latest_version} available! Downloading...")
        if download_update(update_url):
            print("Update downloaded. Restarting...")
            restart_program()
    else:
        print("No updates available.")