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

sign_up_bp = Blueprint("sign_up", __name__,
                  template_folder="templates")

# Sign up system 

@sign_up_bp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
   if request.method == 'POST':
     return register_user(request.form['email'], 
                         request.form['user_name'],
                         request.form['password1'])
   else:
      if "user" in session:
         return redirect(url_for('home.home'))
      return show_the_sign_up_form()

def show_the_sign_up_form():
   return render_template('sign_up.html',sign_up_form=url_for('sign_up.sign_up'))


def register_user(e, u, p):
   query = f"INSERT INTO users (user_name, user_password, user_email)\
               VALUES ('{u}', '{p}', '{e}');"
   register = run_query.run_query(query)
   try:
      if (len(register) == 0):
         flash('user registered','info')
         return redirect(url_for('login.login'))
   
   except:
      flash('Error, try again', 'alert-danger')
      return redirect(url_for('sign_up.sign_up'))