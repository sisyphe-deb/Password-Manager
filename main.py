#!/usr/bin/env python3
import subprocess
import random
import os
import time
import json
import argparse

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Define the path to data.json in the same directory as the script
data_file = os.path.join(script_dir, "data.json")

# Characters to use in password generation
ascii_chars = [chr(i) for i in range(32, 127)]

# Clear terminal screen
def clear():
    os.system("clear")

# Generate a password and store it with the app name
def generate(length=15):
    app = input("For which usage: ")
    psw = ''.join(random.choices(ascii_chars, k=length))
    clear()
    print(f"Generated password for {app} is: {psw}")

    entry = {"app": app, "password": psw}

    # Load existing data or initialize empty list
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new entry
    data.append(entry)

    # Save data to JSON file
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

# Display all saved passwords
def read():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("The file is empty or corrupted.")
                return
        print("Here are the saved passwords:\n")
        for i, entry in enumerate(data, 1):
            app = entry.get("app", "Unknown")
            psw = entry.get("password", "Not defined")
            print(f"{i}. {app} → {psw}")
        print("\n")
    else:
        print("No password file found.")

# Update the CLI tool from GitHub
def update():
    repo_url = "https://github.com/sisyphe-deb/Password-Manager"
    install_path = "/usr/local/bin/psw"

    print("Downloading latest version from GitHub...")

    try:
        subprocess.run(["git", "clone", "--depth", "1", repo_url, "/tmp/psw-update"], check=True)
        subprocess.run(["sudo", "cp", "/tmp/psw-update/main.py", install_path], check=True)
        subprocess.run(["sudo", "chmod", "+x", install_path], check=True)
        print("Update complete.")
    except subprocess.CalledProcessError:
        print("Update failed.")
    finally:
        subprocess.run(["rm", "-rf", "/tmp/psw-update"])

# Interactive text menu
def menu():
    while True:
        print("1- Generate Password")
        print("2- View Passwords")
        print("3- Exit")
        reply = input("Enter your choice: ")

        if reply == "1":
            clear()
            generate()
        elif reply == "2":
            clear()
            read()
        elif reply == "3":
            print("--- See you soon! ---")
            break
        else:
            print("--- Invalid choice ---")
            time.sleep(1)
            clear()

# Entry point with CLI support
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # generate
    gen_parser = subparsers.add_parser("generate", help="Generate a password")
    gen_parser.add_argument("-l", "--length", type=int, default=15, help="Length of the password")

    # read
    subparsers.add_parser("read", help="Show saved passwords")

    # update
    subparsers.add_parser("update", help="Update the tool from GitHub")

    args = parser.parse_args()

    if args.command == "generate":
        generate(args.length)
    elif args.command == "read":
        read()
    elif args.command == "update":
        update()
    else:
        # If no CLI command, show interactive menu
        menu()
