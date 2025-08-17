# 🌷 NoteNest – Your Cozy Encrypted Note Garden 🌸

Welcome to NoteNest – a simple yet secure Python CLI App where your thoughts bloom like flowers 🌼.
It’s a note-taking application with encryption to keep your secrets safe while giving you a fun, garden-inspired CLI experience!

---

## ✨ Features

🔐 Secure Authentication
Setup once with a master username & password.

🗝 Encryption
All notes are encrypted using Fernet (AES under the hood).

🌼 Add Notes – Save your thoughts, todos, or secret recipes.

🌸 View Notes – Display all your saved notes in a beautiful garden-style layout.

🗑 Delete Notes – Remove notes you no longer need.

---

## 🛠 Tech Stack
👩‍💻 Programming Language
  Python 3.8+ – core language for building the CLI application

🔐 Security & Encryption
  hashlib (SHA-256) – password hashing for authentication
  cryptography.fernet – industry-standard AES-based encryption/decryption for notes

🗄 Data Storage
  JSON Files – lightweight storage for:
  notes.json → encrypted notes
  auth.json → username + hashed password
  session.json → login session tracking
  secret.key → Fernet encryption key

🖥 CLI & UX
  argparse – command-line interface (parsers & subcommands)
  getpass – secure password input (no echo on screen)
  Custom ASCII/Emoji prompts – to make the experience fun 🌸🌼

⚙️ Standard Libraries Used
  os  – file handling & existence checks
  sys – program exit handling
  json – data serialization (saving/loading notes & sessions)
---


## ⚙️ Installation  
  bash
  git clone https://github.com/yourusername/NoteNest.git
  cd NoteNest
  pip install cryptography
  python main.py

⚡ Quick start:
  bash
  python main.py Setup
  python main.py Login
  python main.py Add (by getting input from the user)
  python main.py View

## 🖥 Usage Commands
  Command	                           Description
python main.py Setup              🌱 Setup account (one-time)
python main.py Login	            🔑 Login to NoteNest
python main.py Logout	            🚪 Logout
python main.py Add	              🌼 Add a new note (asks for title & content)
python main.py View	              🌸 View all notes
python main.py Delete "Title"   	🗑 Delete a note

## 📂 Project Structure
```
NoteNest/
│── main.py          # CLI entry point (Add, View, Delete, Login, Logout, Setup)
│── auth.py          # Handles authentication (setup, login, logout, session)
│── secure_store.py  # Encryption & decryption logic (Fernet key handling)
│
│── notes.json       # Encrypted notes storage (auto-created)
│── auth.json        # Stores username & hashed password (auto-created)
│── session.json     # Tracks login sessions (auto-created)
│── secret.key       # Encryption key (auto-generated, required for decryption)

```
## 👨‍💻 Contributor
Hi! I’m Akanksha Kurial 🌻 – I enjoy blending tech + creativity.
This project reflects my love for making tools that are not only functional but also fun to use.

⭐ If you like NoteNest, don’t forget to star the repo!
- [Akkukurial448](https://github.com/Akkukurial448)

