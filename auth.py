def login():
    USERNAME = "admin"
    PASSWORD = "1234"

    print("\n--- Admin Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials!\n")
        return False