import os

def write_note():
    note = input("Write your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("✅ Note saved!\n")

def view_notes():
    if not os.path.exists("notes.txt"):
        print("⚠️ No notes found.\n")
        return
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        if not notes:
            print("📭 No notes to show.\n")
        else:
            print("\n📒 Your Notes:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
            print()

def clear_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == "yes":
        open("notes.txt", "w").close()
        print("🧹 All notes cleared!\n")
    else:
        print("❌ Clear cancelled.\n")

def main():
    while True:
        print("=== Simple Notepad ===")
        print("1. Write a note")
        print("2. View notes")
        print("3. Clear all notes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            write_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            clear_notes()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
