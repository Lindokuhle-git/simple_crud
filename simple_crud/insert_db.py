import sqlite3
# from . import get_db, close_db, init_db
from ._database_handler import *


def insert_data(table_name, columns, values):
    """
    Insert data into the specified table.

    Parameters:
        table_name (str): The name of the table to insert data into.
        columns (list): A list of tuples where each tuple contains the column name (str)
                        and its data type (str) in the format 'column_name data_type'.
                        For example: [('column1', 'TEXT'), ('column2', 'INTEGER')]
        values (tuple): A tuple containing the values to be inserted into the columns
                        in the same order as specified in the 'columns' parameter.
    
    Example:
        # Insert a new employee record into the 'employees' table
        table_name = "employees"
        columns = [("name", "TEXT"), ("age", "INTEGER"), ("email", "TEXT")]
        values = ("Alice", 30, "alice@example.com")
        insert_data(table_name, columns, values)

    Raises:
        sqlite3.Error: If there is an error executing the SQL query.
    """                    

    try:
        db = get_db()
        cursor = db.cursor()
        # Construct the column names part of the query
        column_names = ", ".join(col_name for col_name, col_type in columns)

        # Construct the placeholders for values part of the query
        value_placeholders = ", ".join("?" for _ in columns)

         # Construct the complete INSERT query
        query = f'''
        INSERT INTO {table_name} (
            {column_names}
        )
        VALUES (
            {value_placeholders}
        )
        '''

         # Execute the query with the provided values
        cursor.execute(query, values)
        db.commit()
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()