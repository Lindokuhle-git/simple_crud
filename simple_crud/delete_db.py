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