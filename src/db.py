import sqlite3

class Database:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_logs(self, logs):
        # Insert logs into database
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS logs (timestamp TEXT, level TEXT, message TEXT)')
        for log in logs:
            cursor.execute('INSERT INTO logs VALUES (?, ?, ?)', (log['timestamp'], log['level'], log['message']))
        conn.commit()
        conn.close()