import hashlib
import getpass
import json
import os

AUTH_FILE = "auth.json"       # stores single account { "username": "...", "password": "<sha256>" }
SESSION_FILE = "session.json" # stores {"LoggedIn": True, "username": "..."}

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_hashed_password():
    """First-time setup: create username & password (won't overwrite existing)."""
    if os.path.exists(AUTH_FILE):
        print("⚠️ Account already exists. Use Login instead.")
        return
    username = input("👤 Create a username: ").strip()
    while not username:
        print("❌ Username cannot be empty.")
        username = input("👤 Create a username: ").strip()
    password = getpass.getpass("🔑 Create a master password: ")
    confirm = getpass.getpass("🔑 Confirm password: ")
    if password != confirm:
        print("❌ Passwords do not match!")
        return
    data = {"username": username, "password": hash_password(password)}
    with open(AUTH_FILE, "w") as f:
        json.dump(data, f)
    print("✅ Account setup complete.")

def login_user():
    """Login and start a session (creates session.json)."""
    if not os.path.exists(AUTH_FILE):
        print("❌ No account found. Please run: python main.py Setup")
        return
    with open(AUTH_FILE, "r") as f:
        account = json.load(f)
    username = input("👤 Enter username: ").strip()
    if username != account["username"]:
        print("❌ No account found for this username.")
        return
    password = getpass.getpass("🔑 Enter password: ")
    if hash_password(password) == account["password"]:
        with open(SESSION_FILE, "w") as s:
            json.dump({"LoggedIn": True, "username": username}, s)
        print(f"✅ Logged in as {username}.")
    else:
        print("❌ Incorrect password.")

def logout():
    """End the current session (delete session.json)."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
        print("🚪 Logged out successfully.")
    else:
        print("⚠️ You are not logged in.")

def is_logged_in():
    """Return True if session.json indicates logged in."""
    if not os.path.exists(SESSION_FILE):
        return False
    try:
        with open(SESSION_FILE, "r") as f:
            session = json.load(f)
            return session.get("LoggedIn", False)
    except Exception:
        return False

def require_login():
    """Helper: return True if logged in, else print message and return False."""
    if not is_logged_in():
        print("❌ Please log in first! Use: python main.py Login")
        return False
    return True