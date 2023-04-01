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

from access_database import run_query


home_bp = Blueprint("home", __name__,
                  template_folder="templates")

@home_bp.route("/")
def home():
    # user already logged in 
    if "user" in session:
       #send this info to home page so login can be changed dynamically
       flash(f"logged in as: {session['user']}", "info")

    # load books 
    get_books = run_query.run_query("SELECT * FROM books;")
   
    return render_template('home.html', books=get_books)


order_list = []

@home_bp.route("/add", methods=['POST'])
def add_book_to_cart():
   try:
      if request.method == 'POST':
         item = request.form['item']
         item = int(item)
         order_list.append(item)
         session['items'] = order_list

   except:
         flash(f"Error While adding item to cart","info")
         return redirect(url_for('home.home'))


   finally:
      flash(f"Items in cart: {len(session['items'])}","info")
      return redirect(url_for('home.home'))


