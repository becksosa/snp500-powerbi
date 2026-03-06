from dotenv import load_dotenv
import psycopg2
import os

# This function is used to execute SQL queries against the PostgreSQL database
load_dotenv()


def run_query(query, params=None):
    conn = psycopg2.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    try:
        output = cursor.fetchall()
    except psycopg2.ProgrammingError:
        output = None  # No results for INSERT/UPDATE queries
    conn.commit()
    cursor.close()
    conn.close()
    return output
