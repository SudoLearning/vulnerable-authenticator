class BasicAuthenticator:
    def __init__(self):
        self.user_data = {
            "alice": "password123",
            "bob": "secret456",
            "eve": "qwerty789"
        }
    
    def add_user(self, username, password):
        if username not in self.user_data.keys():
            self.user_data[username] = password

    def update_password(self, username, current_password, new_password):
        if self.user_data[username] == current_password:
            self.user_data[username] = new_password
        else:
          print("BE GONE HACKER!")

    def authenticate(self, username, password):
        stored_password = self.user_data.get(username)
        if stored_password == password:
            print(f"Welcome, {username}!")
        else:
            print("Invalid credentials. Calling 911.")

if __name__ == "__main__":
    authenticator = BasicAuthenticator()
    target_user = "alice"
    stored_password = authenticator.user_data.get(target_user)
    print(f"Password for {taregt_user}: {stored_password}")
    authenticator.authenticate(target_user,stored_password)
