import psycopg2
from config import config

def create_tables():
    commands = (
        """
        CREATE TABLE players (
            player_id SERIAL PRIMARY KEY,
            player_name VARCHAR(255) NOT NULL,
            player_score INTEGER NOT NULL
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()