import os
import sqlite3

from .create_db import create_table
import delete
import read_db
import update_db


CONFIG_DB_NAME = ""

def set_CONFIG_DB_NAME(value):
    global CONFIG_DB_NAME
    CONFIG_DB_NAME = value


def get_db():
    conn = None

    if os.path.exists(CONFIG_DB_NAME):
    # Open the existing database
        conn = sqlite3.connect(CONFIG_DB_NAME, check_same_thread=False)
    else:
        # Create a new database and connect to it
        conn = sqlite3.connect(CONFIG_DB_NAME)
    return conn    


def close_db():
    db = getattr(get_db, 'db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())        