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

cart_bp = Blueprint("cart", __name__,
                  template_folder="templates")

@cart_bp.route("/cart")
def cart():
    # show items in cart from session 
    return render_template('cart.html')





     