import os
import sqlite3
import unittest
from simple_crud.read_db import read_table
from simple_crud._database_handler import set_CONFIG_DB_NAME


# Define the test database name
CONFIG_DB_NAME = "test_read_database.db"
set_CONFIG_DB_NAME("test_read_database.db")


def get_db():
    return sqlite3.connect(CONFIG_DB_NAME)

def close_db():
    db = get_db()
    db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()
    # Initialize any necessary setup for the database here
    # db.commit()
    # db.close()

class TestReadTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()
        os.remove(CONFIG_DB_NAME)

    def test_read_table(self):
        # Define the test table name
        table_name = "test_table"

        # Create a test table and insert some data
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        cursor.executemany(f"INSERT INTO {table_name} (name) VALUES (?)", [("Alice",), ("Bob",), ("Charlie",)])
        db.commit()

        # Call read_table to read data from the test table
        data = read_table(table_name)

        # Assert that the data matches the inserted values
        expected_data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
        self.assertEqual(data, expected_data, "Read data does not match the expected values.")
        db.close()

if __name__ == "__main__":
    unittest.main()
