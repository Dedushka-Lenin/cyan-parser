import signal
import sys
import sqlite3

from app.core.config import DB_PATH


class DbConnector:
    _instance = None
    _cursor = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self, db_path=DB_PATH):
        db_path = db_path

        self._connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._cursor = self._connection.cursor()

        signal.signal(signal.SIGINT, self.handle_sigint)

    def get(self):
        if not self._cursor:
            self.connect()
        return  self._connection, self._cursor

    def commit(self):
        if self._connection:
            self._connection.commit()

    def handle_sigint(self, signum, frame):
        self.close()
        sys.exit(0)

    def close(self):
        if self._cursor:
            self._cursor.close()
            self._cursor = None
        if self._connection:
            self._connection.close()
            self._connection = None