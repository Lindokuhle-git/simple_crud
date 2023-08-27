import sqlite3
# from . import get_db, close_db, init_db
from ._database_handler import *

def read_table(table_name):
    """Read data from the specified table.

    Parameters:
        table_name (str): The name of the table to be read from.

    Returns:
        The data in a table as a list
    Raises:
        sqlite3.Error: If there is an error executing the SQL query.        

    """
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f'''SELECT * FROM {table_name}''')
        data = cursor.fetchall()
        return data if data is not None else []
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()     


def read_specified_data(table_name, condition_data):
    """reads the specified row/data from the table in a database.

    Parameters:
        table_name (str): The name of the table to read from.
        condition_data (dict): A dictionary containing column-value pairs to define the condition.

    Example:
        # Read the data from table for all records where 'name' is 'Alice'
        table_name = "employees"
        condition_data = {"name": "Alice"}
        read_specified_data(table_name, condition_data)         

    Raises:
        sqlite3.Error: If there is an error executing the SQL query.        

    """
    
    condition_clause = ' '.join(f"{column} = ?" for column, value in condition_data.items())
    condition_values = tuple(condition_data.values())

    try:
        db = get_db()
        cursor = db.cursor()
        data_query = f'''SELECT * FROM {table_name}  WHERE {condition_clause}'''
        print(data_query)
        cursor.execute(data_query, condition_values)
        data = cursor.fetchall()
        return data if data is not None else []
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()         