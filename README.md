# simple_crud
Simple CRUD is a Python package designed to **simplify the process of working with SQLite databases** for basic CRUD (Create, Read, Update, Delete) operations. It provides a set of utility functions and modules to interact with SQLite databases in a straightforward and user-friendly way.

## Features
- Create Tables: Easily create database tables with specified columns and data types.
- Read Data: Retrieve data from database tables using customizable queries.
- Update Data: Update records in a table based on specified conditions.
- Delete Data: Delete records from a table based on specified conditions.
- Database Management: Initialize and manage SQLite databases effortlessly.

## Database 
This package is built using the sqlite3 (as this DBMS is provided as a python builtin tool) and currently can be used with it. 

## What to download to run the project:
Your PC must have python3 to run the project. The python programming language can be downloaded using this following link:
https://www.python.org/downloads/

## Installing package:
For any project you want to use it for, You can use the command : 
`pip install git+https://github.com/Lindokuhle-git/simple_crud.git`

<img width="446" alt="image" src="https://github.com/Lindokuhle-git/simple_crud/assets/80815469/cf349839-12d9-4cc7-9c85-e85e8c81eab2">


It should start installing on your local pc 

<img width="617" alt="image" src="https://github.com/Lindokuhle-git/simple_crud/assets/80815469/7f6502a3-f11c-46ca-bc05-df58fd837673">


## Using simple_crud in your project:
### Basic Usage

```from simple_crud import CONFIG_DATABASE, TEXT, INTEGER, REAL, create_table, read_table, update_table, delete_table
# Create databse and establish database connection
CONFIG_DATABASE = "mysqlite.db"

# Create a table
# Note the Primary key column is automatically created
table_name = "example_table"
columns = [
    ("name", TEXT),
    ("age", SQL_INTEGER)
]
create_table(table_name, columns)

# Insert data into the table
columns = [("name", TEXT), ("age", SQL_INTEGER), ("email", SQL_INTEGER)]
        values = ("Alice", 30, "alice@example.com")
        insert_data(table_name, columns, values)

# Read data from the table
result = read_table(table_name)
print(result)

# Update data in the table
update_data = {"age": 31}
condition_data = {"name": "Bob"}
update_table(table_name, update_data, condition_data)

# Delete data from the table
condition_data = {"age": 25}
delete_table(table_name, condition_data)

# Delete table
delete_table(table_name)
```
---

## Contributing
We welcome contributions! If you would like to contribute to this project, please reach out using this email specified in the **troubleshoots section**.

## Troubleshooting the Package:
Should any issues arise while using the package: 
~ Use the [issues board](https://github.com/Lindokuhle-git/simple_crud/issues) on github for the project you have issues with, you can assign me and I will comment back as soon as I get the time.

OR : You can email me at lindokuhlerajuili@gmail.com with the name of the project as the subject.
