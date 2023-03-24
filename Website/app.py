from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
from flask import session
from flask import flash
import sqlite3
from flask import g
import functools
import os

app = Flask(__name__)
app.secret_key = 'book_shop'

@app.route("/")
def home():
    # user already logged in 
    if "user" in session:
       flash(f"Already logged: {session['user']}", "info")
    return render_template("index.html")



# Login system 

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
     return do_the_login(request.form['uname'], request.form['pwd'])
   else:
      if "user" in session:
         return redirect(url_for('home'))
      return show_the_login_form()

def show_the_login_form():
   return render_template('login.html',login_form=url_for('login'))



def do_the_login(u,p):
   if (p == 'password'):
      session['user'] = u
      return redirect(url_for('home'))
   else:
      abort(403)

# logout 
@app.route('/logout')
def logout():
    session.pop('user', None) 
    flash("You have been logged out","info") 
    return redirect(url_for('home')) 





if __name__ == "__main__":
    app.run(debug=True)