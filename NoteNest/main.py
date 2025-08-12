from auth import check_password, save_hashed_password, logout
import argparse
import json
import os

STORAGE_FILE = "notes.json"

def load_notes():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(STORAGE_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"✅ Note '{title}' added.")

def view_notes():
    notes = load_notes()
    if not notes:
        print("📭 No notes found.")
        return
    for idx, note in enumerate(notes, 1):
        print(f"\n📌 {idx}. {note['title']}\n{note['content']}")

def delete_note(title):
    notes = load_notes()
    new_notes = [n for n in notes if n['title'] != title]
    if len(notes) == len(new_notes):
        print(f"⚠ No note found with title '{title}'")
    else:
        save_notes(new_notes)
        print(f"🗑 Note '{title}' deleted.")
def main():
    parser = argparse.ArgumentParser(description="NoteNest - CLI Notes App")
    subparsers = parser.add_subparsers(dest="command")

    # Setup password
    subparsers.add_parser("setup", help="Setup master password")
    subparsers.add_parser("logout", help="Logout current session")


    # Add note
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("title", help="Title of the note")
    add_parser.add_argument("content", help="Content of the note")

    # View notes
    subparsers.add_parser("view", help="View all notes")

    # Delete note
    del_parser = subparsers.add_parser("delete", help="Delete a note")
    del_parser.add_argument("title", help="Title of the note to delete")

    args = parser.parse_args()
    print(f"Command received: {args.command}")

    if args.command == "setup":
        save_hashed_password()
    
    elif args.command == "logout":
       logout()


    elif args.command == "add":
        if check_password():
            add_note(args.title, args.content)

    elif args.command == "view":
        if check_password():
            view_notes()

    elif args.command == "delete":
        if check_password():
            delete_note(args.title)

    else:
        parser.print_help()

main()