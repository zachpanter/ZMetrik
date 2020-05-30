import sqlite3
from sqlite3 import Error
from collections import namedtuple
import pdb
from decimal import *
from flask import Flask

app = Flask(__name__)

# TODO: IMPLEMENT
@app.route("/api/morphometriks")
def get_morphometrik_data()


# TODO: IMPLEMENT
@app.route("/api/nahrung")
def get_nahrung_data()


# TODO: IMPLEMENT
@app.route("/api/rauminhalt")
def get_rauminhalt_data()


def create_connection():
    database = r"zmetrik.db"
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn


def calc_one_rep_max(metrik):
    weight = float(metrik[1])
    reps = float(metrik[2])
    #pdb.set_trace()
    returnval = weight * (1 + (reps / 30))
    return returnval


def get_current_one_rep_max(conn, lift_id):
    #pdb.set_trace()
    sql = "SELECT current_one_rep_max FROM lifts WHERE lift_id = ?"
    cur = conn.cursor()
    cur.execute(sql, str(lift_id))
    return cur.fetchone()[0]


def possible_new_pr(conn, current_one_rep_max, metrik):
    possible_pr = calc_one_rep_max(metrik)

    sql = "UPDATE lifts SET current_one_rep_max = ? WHERE lift_id = ?"    

    if (possible_pr > current_one_rep_max):
        cur = conn.cursor()
        sql_data = (possible_pr, metrik[0])
        cur.execute(sql, sql_data)
        conn.commit()


def insert_set(conn, metrik):
    sql = "INSERT INTO metriks (lift_id, weight, reps, intensity) VALUES(?,?,?,?)"
    #pdb.set_trace()
    try:
        current_one_rep_max = get_current_one_rep_max(conn, metrik[0])
        getcontext().prec = 2
        intensity = Decimal(metrik[1]) / Decimal(current_one_rep_max)
        possible_new_pr(conn, current_one_rep_max, metrik)

        sql_data = (metrik[0], metrik[1], metrik[2], float(intensity))
        cur = conn.cursor()
        pdb.set_trace()
        cur.execute(sql, sql_data)
        conn.commit()
    except Error as e:
        print(e)

def list_lifts(conn):
    sql = "SELECT lift_id, title FROM lifts"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    conn = create_connection()

    while True:
        print("What was the weight?")
        weight = input()

        print("What were the reps?")
        reps = input()
        
        print("Which lift?")
        list_lifts(conn)
        lift_id = input()
        
        #Metrik = namedtuple('metrik', 'lift_id weight reps')
        #metrik = Metrik(lift_id, weight, reps)  
        metrik = (lift_id, weight, reps) 
        insert_set(conn, metrik)
        conn.close()

        # pdb.set_trace()
        # print("Input another? Y or N")
        # answer = input()
        # if (answer == "n"):
        #     break
