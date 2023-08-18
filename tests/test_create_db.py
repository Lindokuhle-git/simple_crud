import sqlite3
import unittest
from simple_crud import create_table, get_db, close_db, init_db

# Define the test database name
CONFIG_DB_NAME = "test_database.db"

class TestCreateTable(unittest.TestCase):

    def setUp(self):
        init_db()

    def tearDown(self):
        close_db()

    def test_create_table(self):
        # Define the test table name and columns
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

        # Assert that the columns exist in the table
        cursor.execute(f"PRAGMA table_info({table_name})")
        table_info = cursor.fetchall()
        for col_name, col_type in columns:
            column_exists = any(col_name == col[1] and col_type in col[2] for col in table_info)
            self.assertTrue(column_exists, f"Column '{col_name}' with type '{col_type}' does not exist in the table '{table_name}'.")
        
if __name__ == "__main__":
    unittest.main()
