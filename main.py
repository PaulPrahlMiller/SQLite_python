import sqlite3

from sqlite3 import Error

def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")

    return connection

def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "db"

    company_table = """CREATE TABLE IF NOT EXISTS company (
        id integer PRIMARY KEY,
        name text NOT NULL,
        location text NOT NULL
    );"""

    connection = create_connection(database)

    if connection is not None:
        create_table(connection, company_table)
    else:
        print('Error: Could not connect to database')


if __name__ == '__main__':
    main()