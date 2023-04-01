import sqlite3

# function which connects to databse and runs given query 
def run_query(query):
    con = sqlite3.connect('Website/book_website.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.commit() 
    con.close() 
    return data



# Example 
#e = 'user4@gamil.com'
#u = 'user4'
#p = '12345'
#q = f"INSERT INTO users (user_name, user_password, user_email)\
 #       VALUES ('{u}', '{p}', '{e}');"

#print(len(run_query(q)))

