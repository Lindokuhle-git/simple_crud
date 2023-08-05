# test_your_module_name.py

import sqlite3
import unittest
from CRUD.create_db import create_table
# from CRUD import create_db, get_db, close_db, init_db


CONFIG_DB_NAME = "test_database.db"

# Define the get_db, close_db, and init_db functions (if they are part of your module)
def get_db():
    return sqlite3.connect(CONFIG_DB_NAME)

def close_db():
    db = get_db()
    db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()
    # Initialize any necessary setup for the database here
    db.commit()
    db.close()

class TestCreateTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()
    

    def test_create_table(self):
        table_name = "test_table"
        columns = [
            ("column1", "INTEGER"),
            ("column2", "TEXT"),
            ("column3", "REAL")
        ]

        # Call create_table to create the test table
        create_table(table_name, columns)

        # Assert that the table exists in the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        self.assertIsNotNone(result, f"Table '{table_name}' does not exist in the database.")
        db.close()

# if __name__ == "__main__":
#     unittest.main()
