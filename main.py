import psycopg2
from psycopg2 import sql

# Code to connect to my database and run queries
def main():
    # Connect to the database
    try:
    conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return

        try:
            # Example query
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except Exception as error:
            print(f"Error executing query: {error}")
        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    if __name__ == "__main__":
        main()



