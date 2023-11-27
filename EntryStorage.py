# EntryStorage.py
import csv
from datetime import datetime
from Entry import Entry

class EntryStorage:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_all_entries(self):
        return self.entries

    def save_to_file(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for entry in self.entries:
                writer.writerow([entry.date, entry.time, entry.text])

    def load_from_file(self, filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.entries = [Entry(row[0], row[1], row[2]) for row in reader]

    def search_entries(self, search_term):
        return [entry for entry in self.entries if search_term.lower() in entry.text.lower() or search_term in entry.date]

    def sort_entries(self):
        self.entries.sort(key=lambda entry: datetime.strptime(entry.date + ' ' + entry.time, '%Y-%m-%d %H:%M'))
