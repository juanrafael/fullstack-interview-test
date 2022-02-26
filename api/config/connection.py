import imp
import psycopg2

USER="root"
PASSWORD="root"
HOST="gitapp_db"
PORT="5432"
DATABASE="gitapp"

class Connection:

    def __init__(self) -> None:
        self.conn = psycopg2.connect(user=USER,
                                    password=PASSWORD,
                                    host=HOST,
                                    port=PORT,
                                    database=DATABASE)
        self.cursor = self.conn.cursor()

    def get_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_one(self, query, vars):
        self.cursor.execute(query, vars)
        return self.cursor.fetchone()

    def exec(self, query, vars):
        self.cursor.execute(query, vars)

    def commit(self):
        self.conn.commit()