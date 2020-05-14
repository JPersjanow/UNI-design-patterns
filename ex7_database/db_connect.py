import sqlite3
try:
    from db_errors import *
except ModuleNotFoundError:
    from .db_errors import *

class DB:
    def __init__(self, db):
        self.db_name = db
        self.conn = None
        self.connection_status = None
        self.response = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(f'file:{self.db_name}.db?mode=rw', uri=True)
            print(f"[CONNECTION]: Connection succesfull, connected to: {self.db_name} database")
            self.connection_status = 'SUCCESS'
        except sqlite3.Error as e:
            print(f"[ERROR][CONNECTION]: {e}")
            self.connection_status = e

    def close_connection(self):
        if self.conn is not None:
            try:
                self.conn.close()
                print(f"[CONNECTION][CLOSED]")
            except sqlite3.Error as e:
                print(f"[ERROR][CONNECTION]: Connection closing interrupted!")
                print(f"[ERROR][CONNECTION]: {e}")
        else:
            print(f"[INFO][CONNECTION]: Connection already closed!")
    def get_tables(self):
        sql_create_query = f'SELECT name FROM sqlite_master'
        try:
            c = self.conn.cursor()
            c.execute(sql_create_query)
            print(f"[QUERY][SUCCESS]: {sql_create_query}")
            return c.fetchall()
        except sqlite3.Error as e:
            print(f"[QUERY][FAILURE]: Cannot create table! {e}")

    def create_table(self, table_num: str):

        sql_create_query = f'CREATE TABLE IF NOT EXISTS "TABLE{table_num}" ' \
                           f'("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                           f'"name"	TEXT NOT NULL, ' \
                           f'"value"	INTEGER NOT NULL)'

        try:
            self.conn.cursor().execute(sql_create_query)
            print(f"[CREATION]: Created table!")

        except sqlite3.Error as e:
            print(f"[ERROR][CREATION]: Cannot create table! {e}")




if __name__ == '__main__':
    db = DB('ex7')
    db.connect()
    db.get_tables()
