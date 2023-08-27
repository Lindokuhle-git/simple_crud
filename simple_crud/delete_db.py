import sqlite3
from ._database_handler import *

def delete_table(table_name):
    """deletes the specified table from the database.

    Parameters:
        table_name (str): The name of the table to delete.

    Raises:
        sqlite3.Error: If there is an error executing the SQL query.        

    """
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f'''DELETE FROM {table_name}''')
        db.commit()
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()     


def delete_row_in_table(table_name, condition_data):
    """deletes the specified row from the table in a database.

    Parameters:
        table_name (str): The name of the table to delete from.
        condition_data (dict): A dictionary containing column-value pairs to define the condition.

     Example:
        # Delete the data from table for all records where 'name' is 'Alice'
        table_name = "employees"
        condition_data = {"name": "Alice"}
        delete_row_in_table(table_name, condition_data)         

    Raises:
        sqlite3.Error: If there is an error executing the SQL query.        

    """
    
    condition_clause = ' '.join(f"{column} = ?" for column, value in condition_data.items())
    condition_values = tuple(condition_data.values())

    try:
        db = get_db()
        cursor = db.cursor()
        delete_query = f'''DELETE FROM {table_name} WHERE {condition_clause}'''
        cursor.execute(delete_query, condition_values)
        db.commit()
    
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()          