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
#order_list = [1,3,5]
#print(order_list)
#order_list = tuple(order_list)
#print(order_list)
#title = ["Lightning", "False Memory", "The Jester"]
#title = tuple(title)
#print(title)
#q = f"""SELECT * FROM colloborative_filtering_book_data WHERE "Book-Title" In {title} LIMIT 4;"""

#data = run_query(q)

#for i in data:
 #   print(i['Book-Title'])

#print("finish")