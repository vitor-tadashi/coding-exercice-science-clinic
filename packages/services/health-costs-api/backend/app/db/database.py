import psycopg2
from backend.app.core.config import POSTGRES_SERVER, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(host=POSTGRES_SERVER,
                                           user=POSTGRES_USER,
                                           password=POSTGRES_PASSWORD,
                                           dbname=POSTGRES_DB)
        self.cursor = self.connection.cursor()

    def query(self, q, params):
        cursor = self.cursor
        cursor.execute(q, params)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
