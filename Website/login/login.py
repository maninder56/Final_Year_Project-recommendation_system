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


from access_database import run_query

from flask import Blueprint

login_bp = Blueprint("login", __name__,
                  template_folder="templates")

# Login system 

# if POST request is made then run do_the_login function 
# else show the login page 
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
     return do_the_login(request.form['user_name'], request.form['user_password'])
   else:
      if "user" in session:
         return redirect(url_for('home.home'))
      return show_the_login_form()

def show_the_login_form():
   return render_template('login.html',login_form=url_for('login.login'))


# this function checks user name and password againt databse values 
# and return home page if user exists or returs login page with message 
# if user does not exists
def do_the_login(u, p):
   query = f"SELECT user_name FROM users WHERE user_name='{u}' AND user_password='{p}';"
   check = run_query.run_query(query)
   try:
      if (check[0][0] == u):
         session['user'] = u
         return redirect(url_for('home.home'))
   
   except:
      flash('Incorrect username or password', 'alert-danger')
      return redirect(url_for('login.login'))


# clear user data from session 
@login_bp.route('/logout')
def logout():
    session.pop('user', None) 
    flash("You have been logged out","info") 
    return redirect(url_for('home.home')) 