import hashlib
import getpass
import json
import os

AUTH_FILE = "auth.json"
SESSION_FILE = "session.json"

def hash_string(value):
    return hashlib.sha256(value.encode()).hexdigest()

def is_password_set():
    return os.path.exists(AUTH_FILE)

def is_logged_in():
    return os.path.exists(SESSION_FILE)

def save_hashed_password():
    if is_password_set():
        print("🔐 Account already set.")
        return

    username = input("Create a username: ").strip()
    password = getpass.getpass("Create a master password: ")
    confirm = getpass.getpass("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    hashed_user = hash_string(username)
    hashed_pass = hash_string(password)

    with open(AUTH_FILE, "w") as f:
        json.dump({"username": hashed_user, "password": hashed_pass}, f)

    print("✅ Account setup complete.")

def check_password():
    if is_logged_in():
        return True

    if not is_password_set():
        print("❌ No account found. Please run setup first.")
        return False

    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter master password: ")

    hashed_user_input = hash_string(username)
    hashed_pass_input = hash_string(password)

    with open(AUTH_FILE, "r") as f:
        data = json.load(f)
        if data["username"] == hashed_user_input and data["password"] == hashed_pass_input:
            # Save session
            with open(SESSION_FILE, "w") as session:
                json.dump({"status": "logged_in"}, session)
            return True
        else:
            print("❌ Invalid username or password.")
            return False

def logout():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
        print("👋 Logged out successfully.")
    else:
        print("⚠ No active session found.")