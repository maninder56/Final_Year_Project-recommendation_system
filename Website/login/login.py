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

from flask import Blueprint

login_bp = Blueprint("login", __name__,
                  template_folder="templates")

# Login system 

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
     return do_the_login(request.form['uname'], request.form['pwd'])
   else:
      if "user" in session:
         return redirect(url_for('home.home'))
      return show_the_login_form()

def show_the_login_form():
   return render_template('login.html',login_form=url_for('login.login'))

def do_the_login(u,p):
   if (p == 'password'):
      session['user'] = u
      return redirect(url_for('home.home'))
   else:
      abort(403)



# logout 
@login_bp.route('/logout')
def logout():
    session.pop('user', None) 
    flash("You have been logged out","info") 
    return redirect(url_for('home.home')) 