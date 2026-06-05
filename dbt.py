import psycopg

with psycopg.connect("host=192.168.1.55 dbname=test user=postgres password=aaaaaa") as conn:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO test22 (num, data) VALUES (%s, %s)",
            (100, "now'this one"))
        
        conn.commit()
