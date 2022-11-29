import sqlite3
try:
    conn = sqlite3.connect("demography.sqlite")
    cursor = conn.cursor()
    sql_query = """ CREATE TABLE population (
                id integer PRIMARY KEY,
                city text NOT NULL,
                population int NOT NULL
                )"""
    cursor.execute(sql_query)
    conn.commit()
    print("City_population table created successfully")
except:
    print("City_population table creation failed - Maybe table")
finally:
        conn.close()
