import sqlite3

DB_NAME = "identity_governance.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            user TEXT NOT NULL,
            action TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def insert_audit_log(event_type, user, action, status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO audit_logs (event_type, user, action, status)
        VALUES (?, ?, ?, ?)
    """, (event_type, user, action, status))

    connection.commit()
    connection.close()


def get_audit_logs():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT event_type, user, action, status, created_at
        FROM audit_logs
        ORDER BY created_at DESC
    """)

    logs = cursor.fetchall()
    connection.close()

    return logs