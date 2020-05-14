import sqlite3
from sqlite3 import Error


def create_connection():
    database = r"/home/blackjack/code/fitmetrix/sql/fitmetrix.db"
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn


def insert_set(conn, metrik):
    sql = "INSERT INTO metric (lift_id, weight, reps, intensity) VALUES(?,?,?,?)"
    current_one_rep_max = get_current_one_rep_max(metrik.lift_title)
    liftId = get_lift_id(wset.lift_title)
    intensity = metrik.weight / current_one_rep_max
    new_pr_reached = possible_new_pr(wset.lift_title, wset.weight, wset.reps)

    metrik = (liftId, metrik.weight, metrik.reps, intensity)
    cur = conn.cursor()
    cur.execute(sql, metrik)


def get_lift_id(lift_title):
    #TODO: Implement


def main():
    while True:
        print("What was the weight?")
        weight = Input()

        print("What were the reps?")
        reps = Input()


if __name__ == "__main__":
    conn = create_connection()

    while True:
        print("What was the weight?")
        weight = Input()

        print("What were the reps?")
        reps = Input()
        
        print("Which lift?")
        
        // TODO: Define metrik
        
        insert_set(conn, )

        print("Input another? Y or N")
        answer = Input()
        if (answer == "n"):
            break
