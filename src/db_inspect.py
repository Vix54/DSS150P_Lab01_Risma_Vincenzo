"""Minimal PostgreSQL inspection starter."""

import psycopg2

DB_URI = "dbname='dss150p_lab' user='dss150p' password='dss150p_lab' host='localhost' port='5432'"

def main():
    with psycopg2.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_schema, table_name 
                FROM information_schema.tables 
                WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
            """)
            print("--- TABLES ---")
            for row in cur.fetchall():
                print(row)

            cur.execute("""
                SELECT column_name, data_type, is_nullable 
                FROM information_schema.columns 
                WHERE table_name = 'support_tickets' 
                ORDER BY ordinal_position;
            """)
            print("\n--- COLUMNS ---")
            for row in cur.fetchall():
                print(row)

            cur.execute("SELECT COUNT(*) FROM support_tickets;")
            print("\n--- ROW COUNT ---")
            print(cur.fetchone()[0])

            cur.execute("SELECT * FROM support_tickets LIMIT 5;")
            print("\n--- TOP 5 ROWS ---")
            for row in cur.fetchall():
                print(row)

if __name__ == "__main__":
    main()
