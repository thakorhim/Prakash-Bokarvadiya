import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established")
    except sqlite3.Error as e:
        print(e)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed")
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        print("Table created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)
        cursor.close()  

#main function to demonstrate the connection
if __name__ == '__main__':
    #database = "example.db"
    
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")
    
    # perform operations here (if any)
    
    # close the connection
    close_connection(conn)
