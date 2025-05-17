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



ascii = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]



import random
import json

ascii = [chr(i) for i in range(32, 127)]
file = "data.json"

def generate(lenght=15):
    app = input("For which usage: ")
    psw = ''.join(random.choices(ascii, k=lenght))
    clear()
    print(f"Generated password for {app} is: {psw}")

    entry = {
        "app": app,
        "password": psw
    }

    filename = "data.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)



def clear():
    os.system("clear")


def read():
    file = "data.json"
    with open(file, "r") as f:
        data = json.load(f)
        for i, entry in enumerate(data, 1):
            app = entry.get("app", "Inconnu")
            psw = entry.get("password", "Non défini")
            print(f"{i}. {app} → {psw}")
    print("\n")




def menu():
    while True:
        print("1- Generate Password")
        print("2- Wiew Password")
        print("3- Leave")

        reply = input("Enter your choice: ")

        if reply=="1":
            clear()
            generate()
            break
        elif reply=="2":
            clear()
            read()
            break
        elif reply=="3":
            print("--- See you soon ! ---")
            clear()
            break
        else:
            clear()
            print("--- Invalid choice ---")
            time.sleep(1)
        clear()

menu()

