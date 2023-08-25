import os
import sqlite3
import unittest
from simple_crud.update_db import update_table
from simple_crud._database_handler import set_CONFIG_DB_NAME
from tests.test_create_db import CONFIG_DB_NAME


# Define the test database name
CONFIG_DB_NAME = "test_update_database.db"
set_CONFIG_DB_NAME("test_update_database.db")

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

    def test_update_table(self):
        table_name = "test_update_table"

        # Create a test table and insert some data
        db = get_db()
        cursor = db.cursor() 
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
        cursor.executemany(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", [("Alice", 25), ("Bob", 30), ("Charlie", 22)])
        db.commit()

        # Update the records
        update_data = {"age": 40}
        condition_data = {"name": "Alice"}
        update_table(table_name, update_data, condition_data)

        # Retrieve the updated data
        cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", ("Alice",))
        updated_record = cursor.fetchone()

        # Assert that the age has been updated
        self.assertIsNotNone(updated_record, "Updated record not found")
        self.assertEqual(updated_record[2], 40, "Age not updated correctly")

if __name__ == "__main__":
    unittest.main()  