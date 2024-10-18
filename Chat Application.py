class User:
    def __init__(self, username):
        self.username = username
        self.chat_history = []  # List to track messages sent by the user

    def send_message(self, message):
        self.chat_history.append(message)


class ChatApplication:
    def __init__(self):
        self.users = {}
        self.messages = []  # List to store all messages sent in the chat

    def add_user(self, username):
        if username in self.users:
            print("Username already taken. Please choose a different username.")
        else:
            self.users[username] = User(username)
            print(f"User '{username}' added to the chat.")

    def login_user(self, username):
        if username in self.users:
            print(f"User '{username}' logged in.")
            return self.users[username]
        else:
            print(f"User '{username}' not found. Please register first.")
            return None

    def send_message(self, from_user, to_user, message):
        if from_user.username in self.users and to_user.username in self.users:
            user_message = f"{from_user.username} to {to_user.username}: {message}"
            self.messages.append(user_message)  # Store the message in the chat
            from_user.send_message(user_message)  # Save to sender's chat history
            to_user.send_message(user_message)  # Save to receiver's chat history
            print(user_message)  # Print the message to the console
        else:
            print("One or both users not found. Please check the usernames.")

    def view_chat_history(self):
        print("Chat History:")
        for msg in self.messages:
            print(msg)

    def view_user_history(self, user):
        print(f"{user.username}'s Chat History:")
        for msg in user.chat_history:
            print(msg)


# Example usage
if __name__ == "__main__":
    chat_app = ChatApplication()

    # Adding users
    chat_app.add_user("Alice")
    chat_app.add_user("Bob")

    # Logging in users
    alice = chat_app.login_user("Alice")
    bob = chat_app.login_user("Bob")

    # Sending messages between logged-in users
    if alice and bob:  # Ensure both users are logged in
        chat_app.send_message(alice, bob, "Hello, Bob!")
        chat_app.send_message(bob, alice, "Hi Alice, how are you?")
        chat_app.send_message(alice, bob, "I'm good, thanks!")

    # Viewing chat history
    chat_app.view_chat_history()

    # Viewing a specific user's chat history
    chat_app.view_user_history(alice)
    chat_app.view_user_history(bob)
