import sqlite3 as sql

def compute_and(question, bit):
    result = 0

    con = sql.connect("database.db")
    cur = con.cursor()

    result = cur.execute("SELECT curand, responses FROM ands WHERE question=?", (question,)).fetchone()

    if result:
        curand, responses = result
        ret = curand & bit, responses+1
        cur.execute("UPDATE ands SET curand=?, responses=? WHERE question=?", (ret[0], ret[1], question))
    else:
        ret = bit, 1
        cur.execute("INSERT INTO ands (question, curand, responses) VALUES (?, ?, 1)", (question, ret))

    con.commit()
    con.close()
    return ret
