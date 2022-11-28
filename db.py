import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

def connect_to_db():
    conn = sqlite3.connect('demography.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE city_population (
                city_id INTEGER PRIMARY KEY NOT NULL,
                city TEXT NOT NULL,
                population INTEGER NOT NULL
            );
        ''')

        conn.commit()
        print("City_population table created successfully")
    except:
        print("City_population table creation failed - Maybe table")
    finally:
        conn.close()
