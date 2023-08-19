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