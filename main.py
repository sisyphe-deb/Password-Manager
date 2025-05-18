#!/usr/bin/env python3

import random
import os
import time
import json

print('''




         ____   __ _ ___ _____      _____  ____ __| |
        | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
        | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |
        | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
        |_|_ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __
        / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
        | (_| |  __/ | | |  __/ | | (_| | || (_) | |
        \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|
        |___/



        ''')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "data.json")

ascii = [chr(i) for i in range(32, 127)]

def generate(lenght=15):
    app = input("For which usage: ")
    psw = ''.join(random.choices(ascii, k=lenght))
    clear()
    print(f"Generated password for {app} is: {psw}")

    entry = {
        "app": app,
        "password": psw
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def clear():
    os.system("clear")

def read():
    if not os.path.exists(DATA_FILE):
        print("No data available.\n")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        for i, entry in enumerate(data, 1):
            app = entry.get("app", "Inconnu")
            psw = entry.get("password", "Non défini")
            print(f"{i}. {app} → {psw}")
    print("\n")

def menu():
    while True:
        print("1- Generate Password")
        print("2- View Password")
        print("3- Leave")

        reply = input("Enter your choice: ")

        if reply == "1":
            clear()
            generate()
            break
        elif reply == "2":
            clear()
            read()
            break
        elif reply == "3":
            print("--- See you soon ! ---")
            clear()
            break
        else:
            clear()
            print("--- Invalid choice ---")
            time.sleep(1)
        clear()

menu()
