#!/usr/bin/python
from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("demography.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/city", methods=["GET", "POST"])
def getdetails():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM population")
        getdetails = [
            dict(id=row[0], city=row[1], population=row[2])
            for row in cursor.fetchall()
        ]
        if getdetails is not None:
            return jsonify(getdetails)

    if request.method == "POST":
        city_name = request.form["city"]
        total_population = request.form["population"]
        sql = """INSERT INTO population(city, population)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql, (city_name,total_population))
        conn.commit()
        return f"Population with the id: 0 created successfully", 201



@app.route('/update/<city>', methods=['PUT'])
def update(city):
    conn = db_connection()
    cursor = conn.cursor()

    city_update = request.form["city"],
    population_update =  request.form["population"]
    sql = """UPDATE population SET city = ?, population = ?)
                 VALUES (?, ?)"""
    cursor = cursor.execute(sql, (city_update,population_update))
    conn.commit()
    return json.dumps("Record was successfully updated")




@app.route('/getPopulation/<city>', methods=['GET'])
def get_population_by_city(city):
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM population WHERE city=?", (city,))
    #c = sqlite3.connect("student.db").cursor()
    #c.execute("SELECT * FROM STUDENTS WHERE id=?", (student_id,))
    data = cursor.fetchone()
    return json.dumps(data)


@app.route("/health",methods=['GET'])
def health():
    return 'OK'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug=True)
