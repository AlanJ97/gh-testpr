import psycopg2  # Created by copilot
from psycopg2 import sql  # Created by copilot

# Code to connect to my database and run queries
def main():  # Created by copilot
    # Connect to the database
    try:  # Created by copilot
        conn_copilot = psycopg2.connect(  # Created by copilot
            dbname="postgres",  # Created by copilot
            user="postgres",  # Created by copilot
            password="postgres",  # Created by copilot
            host="localhost",  # Created by copilot
            port="5432"  # Created by copilot
        )
        cursor_copilot = conn_copilot.cursor()  # Created by copilot
    except Exception as error_copilot:  # Created by copilot
        print(f"Error connecting to the database: {error_copilot}")  # Created by copilot
        return  # Created by copilot

    try:  # Created by copilot
        # Example query
        cursor_copilot.execute("SELECT version();")  # Created by copilot
        record_copilot = cursor_copilot.fetchone()  # Created by copilot
        print("You are connected to - ", record_copilot, "\n")  # Created by copilot
    except Exception as error_copilot:  # Created by copilot
        print(f"Error executing query: {error_copilot}")  # Created by copilot
    finally:  # Created by copilot
        # Close the cursor and connection
        cursor_copilot.close()  # Created by copilot
        conn_copilot.close()  # Created by copilot

if __name__ == "__main__":  # Created by copilot
    main()  # Created by copilot



