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
from home.home import order_list

cart_bp = Blueprint("cart", __name__,
                  template_folder="templates")

@cart_bp.route("/cart")
def cart():
    tuple_list = tuple(order_list)
    print(tuple_list)

    try:
        query = f"SELECT * FROM books WHERE book_id IN {tuple_list};" 
        cart_items = run_query.run_query(query)
        if len(cart_items) == 0:
            flash("Cart Emplty", "info")
        return render_template('cart.html', books=cart_items)
    

    except Exception as e:
        print(e)
        flash("Cart Emplty", "info")
        return redirect(url_for('home.home'))
    

@cart_bp.route('/empty')
def empty_cart():
    try:
        order_list.clear()
        session.pop('items',None)
        flash("Cart Cleared","info") 
        return redirect(url_for('cart.cart'))
    
    except Exception as e:
        print(e)



     