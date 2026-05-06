notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")

def add_note():
    title = input("title for new note:")
    text = input("text for new note:")
    new_note = {"title" : title , "text" : text}
    notes.append(new_note)
    print(f"The note {new_note} is added!")

def delete_note():
    title = input("title to remove: ")
    for note in notes:
        if note ["title"] == title:
            notes.remove(note)
            print(f"The note '{title}' was removed!")
        else:
            print(f"This note is missing. ")
    

def update_note():
    title = input("Which note to edit?: ")
    for note in notes:
        if note["title"] == title:
            note["title"] = input("New title: ")
            note["text"] = input("New text: ")
            print("Note updated!!!")

#add_note()
#delete_note()
update_note()
show_notes()
