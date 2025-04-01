import requests
import os
import sys
import subprocess

VERSION_URL = "https://raw.githubusercontent.com/Scavix/another-auto-updater-take/main/latest_version.txt"
UPDATE_URL = "https://github.com/Scavix/another-auto-updater-take/releases/latest/download/calculator.exe"

def get_latest_version():
    """Fetch the latest version from GitHub."""
    try:
        response = requests.get(VERSION_URL)
        return response.text.strip()
    except requests.RequestException:
        return None

def download_update():
    """Download the latest EXE from GitHub Releases."""
    try:
        response = requests.get(UPDATE_URL, stream=True)
        with open("calculator_new.exe", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return "calculator_new.exe"
    except requests.RequestException:
        return None

def restart_program():
    """Replace old EXE and restart."""
    new_file = download_update()
    if new_file:
        os.rename("calculator.exe", "calculator_old.exe")
        os.rename("calculator_new.exe", "calculator.exe")
        subprocess.Popen(["calculator.exe"])
        sys.exit()

def check_and_update():
    """Check for an update and apply if available."""
    current_version = get_current_version()
    latest_version = get_latest_version()
    if latest_version and latest_version > current_version:
        print(f"New version {latest_version} available! Updating...")
        restart_program()
    else:
        print("No updates available.")

def get_current_version():
    """Get the current version from a local file or hardcode it."""
    try:
        with open("current_version.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "0.0"