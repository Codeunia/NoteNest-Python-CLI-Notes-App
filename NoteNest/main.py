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
    parser = argparse.ArgumentParser(description="NoteNest – Simple CLI Notes App")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("title", help="Title of the note")
    add_parser.add_argument("content", help="Content of the note")

    # View
    subparsers.add_parser("view", help="View all notes")

    # Delete
    del_parser = subparsers.add_parser("delete", help="Delete a note")
    del_parser.add_argument("title", help="Title of the note to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.title, args.content)
    elif args.command == "view":
        view_notes()
    elif args.command == "delete":
        delete_note(args.title)
    else:
        parser.print_help()

main()
