#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

def insert_city(city_ppl):
    inserted_city = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO city_population (city, population) VALUES (?, ?)", (city_ppl['city'], city_ppl['population']) )
        conn.commit()
        inserted_city = get_city_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_city


def get_cities():
    city_population = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM city_population")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            city_ppl = {}
            city_ppl["city_id"] = i["city_id"]
            city_ppl["city"] = i["city"]
            city_ppl["population"] = i["population"]
            city_population.append(city_ppl)

    except:
        city_ppl = []

    return city_ppl


def update_user(city_ppl):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE city_population SET city = ?, population = ? WHERE city_id =?", (city_ppl["city"], city_ppl["population"], city_ppl["city_id"],))
        conn.commit()
        #return the user
        updated_user = get_city_by_id(user["city_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user



city_population = []
city0 = {
    "city": "charles@gamil.com",
    "phone": "067765665656",
    "address": "Lui Str, Innsbruck",
    "country": "Austria"
}

city1 = {
    "name": "Sam Adebanjo",
    "email": "samadebanjo@gamil.com",
    "phone": "098765465",
    "address": "Sam Str, Vienna",
    "country": "Austria"
}

city2 = {
    "name": "John Doe",
    "email": "johndoe@gamil.com",
    "phone": "067765665656",
    "address": "John Str, Linz",
    "country": "Austria"
}

city3 = {
    "name": "Mary James",
    "email": "maryjames@gamil.com",
    "phone": "09878766676",
    "address": "AYZ Str, New york",
    "country": "United states"
}

city_population.append(city0)
city_population.append(city1)
city_population.append(city2)
city_population.append(city3)

create_db_table()

for i in city_population:
    print(insert_city(i))




app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/users', methods=['GET'])
def api_get_cities():
    return jsonify(get_cities())

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_city(user))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()