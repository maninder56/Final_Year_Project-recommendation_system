import sqlite3

# function which connects to databse and runs given query 
def run_query(query):
    con = sqlite3.connect('Website/book_website.db')
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.commit() 
    con.close() 
    return data

