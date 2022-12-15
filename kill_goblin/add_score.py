import psycopg2
from config import config


def insert_player(name1, score1):
    sql = "INSERT INTO players(player_name, player_score) VALUES(%s,%s);"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name1, score1))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#if __name__ == '__main__':
#    insert_player("max", 26)

