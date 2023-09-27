import os
import sqlite3
import unittest
from simple_crud.insert_db import insert_data
from simple_crud._database_handler import set_CONFIG_DB_NAME
from tests.test_create_db import CONFIG_DB_NAME


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
    

class TestInsertData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()
        os.remove(CONFIG_DB_NAME)

    def test_insert_data(self):
        table_name = "test_insert_table"
        columns = [("name", "TEXT"), ("age", "INTEGER")]


        values = ("Alice", 25)

    
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")


        insert_data(table_name, columns, values)

        
        cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", ("Alice",))
        result = cursor.fetchone()
        self.assertIsNotNone(result, "Inserted data not found in the table.")

if __name__ == "__main__":
    unittest.main()
