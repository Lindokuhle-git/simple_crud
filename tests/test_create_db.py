import os
import sqlite3
import unittest
from simple_crud.create_db import create_table
from simple_crud._database_handler import set_CONFIG_DB_NAME, TEXT, REAL

# Define the test database name
CONFIG_DB_NAME = "test_create_database.db"
set_CONFIG_DB_NAME("test_create_database.db")


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
        os.remove(CONFIG_DB_NAME)

    def test_create_table(self):
        # Define the test table name and columns
        table_name = "test_table"
        columns = [
            ("column1", TEXT),
            ("column2", TEXT),
            ("column3", REAL)
        ]

        # Call create_table to create the test table
        create_table(table_name, columns)

        # Assert that the table exists in the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        self.assertIsNotNone(result, f"Table '{table_name}' does not exist in the database.")

        # Assert that the columns exist in the table
        cursor.execute(f"PRAGMA table_info({table_name})")
        table_info = cursor.fetchall()
        for col_name, col_type in columns:
            column_exists = any(col_name == col[1] and col_type in col[2] for col in table_info)
            self.assertTrue(column_exists, f"Column '{col_name}' with type '{col_type}' does not exist in the table '{table_name}'.")
        
if __name__ == "__main__":
    unittest.main()
