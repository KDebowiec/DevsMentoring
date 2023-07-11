# Stwórz funkcjonalność prostego notatnika o następujących funkcjonalnościach:
# Dodaj notatkę (użytkownik podaje unikalną nazwę i treść notatki, data utworzenia notatki ustawiana jest automatycznie)
# Usuń notatkę (podajemy nazwę notatki, która ma zostać usunięta)
# Wyświetl wszystkie notatki (wyświetlamy nazwę notatki, treść i datę utworzenia)
import sqlite3
from datetime import datetime

class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Notes(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, text NOT NULL, date);"
        self.con.execute(query)

    def add_note(self, name, text):
        date = datetime.now()
        query = "INSERT INTO Notes(name, text, date) VALUES(?, ?, ?)"
        self.con.execute(query, (name, text, date))

    def delete_note(self, name):
        query = f"DELETE FROM Notes WHERE name = ?"
        self.con.execute(query, (name,))

    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()


with Database('notes-data') as db:
    db.create_table()
    db.add_note('prawda', 'jestem przechuj', )
    db.add_note('falsz', 'umiem programowac')
    db.delete_note('falsz')
    db.preview_table('Notes')
