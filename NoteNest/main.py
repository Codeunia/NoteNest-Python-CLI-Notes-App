import argparse
import json
import os
from cryptography.fernet import InvalidToken
from auth import save_hashed_password, login_user, logout, require_login
from secure_store import generate_key, encrypt_data, decrypt_data

STORAGE_FILE = "notes.json"

generate_key()

def load_notes():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "rb") as f:
        encrypted_data = f.read()
    if not encrypted_data:
        return []
    try:
        decrypted_data = decrypt_data(encrypted_data)
        return json.loads(decrypted_data.decode())
    except InvalidToken:
        print("❌ Cannot decrypt notes. Your encryption key might be missing or changed.")
        return []

def save_notes(notes):
    data = json.dumps(notes, indent=2).encode()
    encrypted_data = encrypt_data(data)
    with open(STORAGE_FILE, "wb") as f:
        f.write(encrypted_data)

# Note actions
def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"🌼✨ Yay! Your note '{title}' has bloomed in the garden! ✨🌼")

def view_notes():
    notes = load_notes()
    if not notes:
        print("📭🌱 No notes yet... let's grow your note garden!")
        return
    print("\n🌸🌿 --- Your Note Garden --- 🌿🌸")
    for idx, note in enumerate(notes, 1):
        print(f"\n🌺 {idx}. {note['title']}\n   📜 {note['content']}")

def delete_note(title):
    notes = load_notes()
    new_notes = [n for n in notes if n['title'] != title]
    if len(notes) == len(new_notes):
        print(f"⚠️🌼 Oops! No note found with the title '{title}'.")
    else:
        save_notes(new_notes)
        print(f"🗑🌸 The note '{title}' has been gently removed from the garden.")

# CLI
def main():
    print("\n🌷🐦 Welcome to NoteNest - Your Cozy Note Garden! 🐦🌷")
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("Setup", help="🌱 Setup master password (one-time)")
    subparsers.add_parser("Login", help="🔑 Login to NoteNest")
    subparsers.add_parser("Logout", help="🚪 Logout from NoteNest")
    add_parser = subparsers.add_parser("Add", help="🌼 Add a new note")
    add_parser.add_argument('-t', '--title', help='Title of the note')
    add_parser.add_argument('-c', '--content', help='Content of the note')
    subparsers.add_parser("View", help="🌸 View all notes")
    del_parser = subparsers.add_parser("Delete", help="🗑 Delete a note")
    del_parser.add_argument("title", help="🌺 Title of the note to delete")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "Setup":
        save_hashed_password()

    elif args.command == "Login":
        login_user()

    elif args.command == "Logout":
        logout()

    elif args.command == "Add":
        if require_login():
            title = args.title or input("Enter note title: ")
            content = args.content or input("Enter note content: ")
            add_note(title, content)

    elif args.command == "View":
        if require_login():
            view_notes()

    elif args.command == "Delete":
        if require_login():
            delete_note(args.title)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()