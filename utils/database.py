import sqlite3

from config import config


def get_db_connection():
    conn = sqlite3.connect(config.DATABASE)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access to rows
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        message TEXT NOT NULL,
                        image BLOB,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()