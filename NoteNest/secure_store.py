from cryptography.fernet import Fernet
import os
import sys

KEY_FILE = "secret.key"

# 🔑 Generate key only if not exists (and never overwrite)
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

# 🔑 Load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        print("❌ Encryption key missing! Cannot decrypt old notes.")
        print("If you lost the key, delete notes.json to start fresh.")
        sys.exit(1)
    with open(KEY_FILE, "rb") as f:
        return f.read()

# 🔐 Encrypt data (bytes)
def encrypt_data(data):
    fernet = Fernet(load_key())
    return fernet.encrypt(data)

# 🔓 Decrypt data (bytes)
def decrypt_data(data):
    fernet = Fernet(load_key())
    return fernet.decrypt(data)
