import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

'''
Implement delete_entry() in the model so that the post with the specified ID is deleted. Make sure that these changes are persisted to entries.json.
'''

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
        if str(entry['id']) == str(id):
            entries.remove(entry)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    next_id = 0
    for entry in entries:
        if entry['id'] >= next_id:
            next_id = entry['id'] + 1
    # print(next_id)
    now = datetime.now()
    # time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": next_id}
    next_id += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
