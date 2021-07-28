from os import name
import sqlite3
from sqlite3 import Error
import datetime

def db_connection_create(db_file) :
    """ create a database connection to a SQLite database 
        specified by db_file
        : param db_file : database file
        : return : Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def db_create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def db_insert_function(conn,values):
    statement = """
                INSERT INTO logs(Services,DateTime,Query,Response,Description,JSON_RESP) 
                VALUES(?,?,?,?,?,?)
                """
    curs = conn.cursor()
    curs.execute(statement,values)
    conn.commit()

def db_update_function(conn, values):
    statement = """
                UPDATE logs 
                SET Services = ?,
                    DateTime = ?,
                    Query = ?,
                    Response = ?,
                    Description = ?,
                    JSON_RESP = ?
                WHERE id = ?
                """
    curs = conn.cursor()
    curs.execute(statement,values)
    conn.commit()

def db_refresh_function(conn):
    statement = """
                UPDATE logs
                """
    curs = conn.cursor()
    curs.execute(statement)
    conn.commit()

def db_delete_function(conn, values):
    statement = """
                DELETE FROM logs WHERE id = ?
                """
    curs = conn.cursor()
    curs.execute(statement,(values,))
    conn.commit()

def db_destroy_function(conn):
    statement = """
                DELETE FROM logs
                """
    curs = conn.cursor()
    curs.execute(statement)
    conn.commit()

def db_display_function(conn):
    statement = """
                SELECT * FROM logs
                """
    curs = conn.cursor()
    curs.execute(statement)
    raws = curs.fetchall()

    for item in raws :
        print(item)

def external_request(mode, value_tuple):
    database_pathway = r"storage.db"
    connection = db_connection_create(database_pathway)
    raw = str(mode)

    if raw == 'cr_tb':
        db_create_table(connection, value_tuple)
    elif raw == 'insert':
        db_insert_function(connection, value_tuple)
    elif raw == 'update':
        db_update_function(connection,value_tuple)
    elif raw == 'refresh':
        db_refresh_function(connection)
    elif raw == 'delete':
        db_delete_function(connection, value_tuple)
    elif raw == 'destroy':
        db_destroy_function(connection)
    elif raw == 'show_all':
        db_display_function(connection)


def db_create():
    dataBase = r"storage.db"
    conn = db_connection_create(dataBase)

    sql_create_log_table = """
                            CREATE TABLE IF NOT EXISTS logs (
                                id integer PRIMARY KEY,
                                Services text NOT NULL,
                                DateTime text NOT NULL,
                                Query text NOT NULL,
                                Response text NOT NULL,
                                Description text NOT NULL,
                                JSON_RESP text NOT NULL
                            );
                           """
    date = str(datetime.datetime.now())
    db_create_table(conn, sql_create_log_table)


def main():
    db = "E:\python_Projects\Mapper\Ild-Mapper\storage.db"
    connection = db_connection_create(db)
    db_destroy_function(connection)

if __name__ == '__main__':
    main()
