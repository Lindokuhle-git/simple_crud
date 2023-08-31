import os
import sqlite3
import unittest
from simple_crud.insert_db import insert_data
from simple_crud._database_handler import set_CONFIG_DB_NAME
from tests.test_create_db import CONFIG_DB_NAME

# Define the test database name
CONFIG_DB_NAME = "test_insert_database.db"
set_CONFIG_DB_NAME("test_insert_database.db")

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

class TestInsertData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()
        os.remove(CONFIG_DB_NAME)

    def test_insert_data(self):
        # Define the test table name and columns
        table_name = "test_insert_table"
        columns = [("name", "TEXT"), ("age", "INTEGER")]

        # Define the test values to insert
        values = ("Alice", 25)

        #create the table
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

        # Call insert_data to insert the test values
        insert_data(table_name, columns, values)

        # Verify that the data has been inserted
        
        cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", ("Alice",))
        result = cursor.fetchone()
        self.assertIsNotNone(result, "Inserted data not found in the table.")

if __name__ == "__main__":
    unittest.main()
