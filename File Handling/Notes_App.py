def add_note(note):
    f=open("Notes.txt",'a')
    f.write(note+'\n')
    f.close()
def view_notes():
    try:
        f=open("Notes.txt",'r')
        lines=f.read()
        print(lines)
        f.close()
    except FileNotFoundError:
        print("File not found")
line='-'*40
while True:
    try:
        print(f"{line}\nWelcome to Notepad\n{line}")
        print("1. Add Note\n2. View Note\n3. Exit\n")
        choice=(int(input("Enter a choice: ")))
        if choice==1:
            note=input("Enter Note: ")
            note=note.strip()
            if note:
                add_note(note)
            else:
                print("Enter a non empty note")
        elif choice==2:
            view_notes()
        elif choice==3:
            print("Thank you for using notepad")
            break
        else:
            print("Enter a valid choice")
    except ValueError:
        print("Please enter a valid integer")