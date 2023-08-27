import os
import sqlite3
import unittest
from simple_crud.delete_db import delete_table, delete_row_in_table
from simple_crud._database_handler import set_CONFIG_DB_NAME
from tests.test_create_db import CONFIG_DB_NAME


# Define the test database name
CONFIG_DB_NAME = "test_delete_database.db"
set_CONFIG_DB_NAME("test_delete_database.db")

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

class TestDeleteTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()
        os.remove(CONFIG_DB_NAME)

    def test_delete_table(self):
        table_name = "test_delete_table"

        # Create a test table and insert some data
        db = get_db()
        cursor = db.cursor() 
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
        cursor.executemany(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", [("Alice", 25), ("Bob", 30), ("Charlie", 22)])
        db.commit()   

        delete_table(table_name) 

        cursor.execute(f"SELECT * FROM {table_name} ")
        updated_record = cursor.fetchall()

        self.assertTrue(len(updated_record) ==0)

    def test_delete_row_in_table(self):
        # Define the test table name
        table_name = "employees"

        db = get_db()
        cursor = db.cursor() 
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
        cursor.executemany(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", [("Alice", 25), ("Bob", 30), ("Charlie", 22)])
        db.commit()  

        condition_data = {"name": "Alice"}

        # Call delete_row_in_table to delete data from the test table
        delete_row_in_table(table_name, condition_data)

        # Verify that the row has been deleted
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", ("Alice",))
        result = cursor.fetchone()
        self.assertIsNone(result, "Row with name 'Alice' still exists in the table.")    


if __name__ == "__main__":
    unittest.main()        