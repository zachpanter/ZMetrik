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


def calc_one_rep_max(metrik):
	return metrik.weight * (1 + (reps / 30))


def get_current_one_rep_max(conn, lift_id)
	sql = "SELECT current_one_rep_max FROM lift WHERE lift_id = ?"
	cur = conn.cursor()
	cur.execute(sql, lift_id)


def possible_new_pr(conn, current_one_rep_max, metrik):
	possible_pr = self.calculate_one_rep_max(metrik)

	sql = "UPDATE lift SET current_one_rep_max = ? WHERE lift_id = ?"	

	if (possible_pr > current_one_rep_max):
		cur = conn.cursor()
		sql_data = (possible_pr, metrik.lift_id)
		cur.execute(sql, sql_data)		


def insert_set(conn, metrik):
    sql = "INSERT INTO metric (lift_id, weight, reps, intensity) VALUES(?,?,?,?)"
    
	current_one_rep_max = self.get_current_one_rep_max(conn, metrik.lift_id)
    intensity = metrik.weight / current_one_rep_max
    possible_new_pr(conn, current_one_rep_max, metrik)

    sql_data = (metrik.lift_id, metrik.weight, metrik.reps, intensity)
    cur = conn.cursor()
    cur.execute(sql, sql_data)


def list_lifts(conn):
	sql = "SELECT lift_id, title FROM lift"
	cur = conn.cursor()
	cur.execute(sql)


if __name__ == "__main__":
    conn = create_connection()

    while True:
        print("What was the weight?")
        weight = Input()

        print("What were the reps?")
        reps = Input()
        
        print("Which lift?")
		self.list_lifts()        
		lift_id = Input()
		
		metrik = (lift_id, weight, reps)        
        insert_set(conn, metrik)

        print("Input another? Y or N")
        answer = Input()
        if (answer == "n"):
            break
