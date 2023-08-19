import sqlite3

from ._database_handler import get_db, close_db

# from . import get_db, close_db, init_db


def create_table(table_name, columns):
    """Create a new table in the SQLite database with the specified table name and columns.

    Parameters:
        table_name (str): The name of the table to be created.
        columns (list): A list of tuples where each tuple contains the column name (str)
                        and its data type (str) in the format 'column_name data_type'.
                        For example: [('column1', 'INTEGER'), ('column2', 'TEXT')]

    Raises:
        sqlite3.Error: If there is an error executing the SQL query.

    Example:
        # Create a table named 'shortenedURL' with columns 'id' (auto-incrementing),
        # 'original_url' (TEXT NOT NULL), and 'shortened_url' (TEXT NOT NULL)
        table_name = "shortenedURL"
        columns = [
            ("original_url", "TEXT NOT NULL"),
            ("shortened_url", "TEXT NOT NULL")
        ]
        create_table(table_name, columns)
    """
    try:
        db = get_db()
        cursor = db.cursor()
        
        column_defs = ", ".join(f"{col_name} {col_type}" for col_name, col_type in columns)
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {column_defs}
        )
        '''

        cursor.execute(query)
        db.commit()
    except sqlite3.Error  as e:
        print(f"An error occurred: {e}")
    finally:
        close_db()    
   
