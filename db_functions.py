import sqlite3

def create_film(con, id, title, type, rating):
    cur = con.cursor()
    cur.execute("INSERT INTO films VALUES (?, ?, ?, ?)",
                (id, title, type, rating))
    con.commit()

def retrieve_film(con, id):
    cur = con.cursor()
    cur.execute("SELECT * FROM films WHERE id = ?", (id,))
    row = cur.fetchone()
    if not row:
        return None
    
    return {
        "id": row[0],
        "title": row[1],
        "type": row[2],
        "rating": row[3]
    }

def retrieve_all_films(con):
    cur = con.cursor()
    return [
        {"id": row[0], "title": row[1], "type": row[2], "rating": row[3]}
        for row in cur.execute("SELECT * FROM films")
    ]

def delete_film(con, id):
    cur = con.cursor()
    cur.execute("SELECT * FROM filsm WHERE id = ?", (id,))
    row = cur.fetchone()
    if row is None:
        return None
    cur.execute("DELETE FROM films WHERE id = ?", (id,))
    con.commit()
    return row[1]

# def update_film(con, id):
#     cur = con.cursor()
#     cur.execute("UPDATE")
    