from db import get_connection
from password_utils import hash_password

def add_user(user_name: str, plain_password: str, email: str):
    hashed_pw = hash_password(plain_password)
    
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO users (user_name, password, email, created_date)
                    VALUES (%s, %s, %s, NOW())
                    RETURNING user_id
                    """,
                    (user_name, hashed_pw, email)
                )
                user_id = cursor.fetchone()[0]
        print(f"add user success user_id = {user_id}")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    add_user("admin", "1234A","admin@gmail.com")