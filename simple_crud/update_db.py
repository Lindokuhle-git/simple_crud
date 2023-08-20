import sqlite3
# from . import get_db, close_db, init_db
from ._database_handler import *

def update_table(table_name, update_data, condition_data):
    """
    Update records in the specified table based on a given condition.

    Parameters:
        table_name (str): The name of the table to update.
        update_data (dict): A dictionary containing column-value pairs to update.
        condition_data (dict): A dictionary containing column-value pairs to define the condition.

    Example:
        # Update the 'age' column to 30 for all records where 'name' is 'Alice'
        table_name = "employees"
        update_data = {"age": 30}
        condition_data = {"name": "Alice"}
        update_table(table_name, update_data, condition_data)
    """
    set_clause = ', '.join(f"{column} = ?" for column, value in update_data.items())
    update_values = tuple(update_data.values())

    condition_clause = ' AND '.join(f"{column} = ?" for column, value in condition_data.items())
    condition_values = tuple(condition_data.values())

    try:
        db = get_db()
        cursor = db.cursor()
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}"
        cursor.execute(update_query, update_values + condition_values)
        db.commit()
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()     