from db import get_connection

def create_users_table():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(100) UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL,
                        created_at TIMESTAMP DEFAULT NOW()
                    )
                               """)
        print("create table users success")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    create_users_table()