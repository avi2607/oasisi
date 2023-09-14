# Sample user database
user_database = {
    'Avi': '4512@Avi',
    'rgv': 'password',
    'hardik': 'password33'
}

def authenticate(username, password):
    if username in user_database and user_database[username] == password:
        return True
    else:
        return False

def main():
    print("Welcome to the login system")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authenticate(username, password):
            print("Authentication successful. You are logged in as", username)
            break
        else:
            print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()
