import sqlite3


class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATE NOT NULL);"
        self.con.execute(query)

    def add_to_customers(self, name, surname, date_joined):
        query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?, ?, ?)"
        self.con.execute(query, (name, surname, date_joined))

    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def delete_customer(self, surname):
        query = f"DELETE FROM Customers WHERE surname = ?"
        self.con.execute(query, (surname,))

    def update_customer(self, customer_id, surname):
        query = f'UPDATE Customers SET surname = ? WHERE id = ?'
        self.con.execute(query, (surname, customer_id))

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()


with Database('example2-data') as db:
    db.create_table()
    db.add_to_customers('John', 'Wick', '2000-09-02')
    db.add_to_customers('James', 'Bond', '2002-05-16')
    db.preview_table('Customers')
    db.delete_customer('Bond')
    db.preview_table('Customers')
    db.update_customer(4, 'Debowiec')
    db.preview_table('Customers')
