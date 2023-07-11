import sqlite3


class Trainings:

    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Trainings(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL, time INTEGER NOT NULL);"
        self.con.execute(query)

    def add_note(self, name, price, time):
        query = "INSERT INTO Trainings(name, price, time) VALUES(?, ?, ?)"
        self.con.execute(query, (name, price, time))

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


class Customers:

    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, trainingID ??);"
        self.con.execute(query)

    def add_note(self, name, price, time):
        query = "INSERT INTO Customers(name, price, time) VALUES(?, ?, ?)"
        self.con.execute(query, (name, price, time))

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