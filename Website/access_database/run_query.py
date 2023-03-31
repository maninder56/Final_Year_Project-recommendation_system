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



# Example 
#u = 'user1'
#p = '12345'
#q = f"SELECT user_name FROM users WHERE user_name='{u}' AND user_password='{p}';"

#print(run_query(q))