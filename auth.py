# auth.py

users = {
    "John doe": "password",
    "Reginna": "securepass"
}

def print_border():
    print("************")

def login():
    print_border()
    print("Welcome to the banking program")
    print_border()
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!\n")
            return username
        else:
            attempts -= 1
            print("Invalid username or password.")
            print(f"Attempts remaining: {attempts}")
    print_border()
    print("Too many failed attempts. Exiting.")
    return None





        