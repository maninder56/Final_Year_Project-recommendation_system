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

# import different section of website 
from home.home import home_bp
from login.login import login_bp
from sign_up.sign_up import sign_up_bp
from cart.cart import cart_bp
from about.about import about_bp
from search.search import search_bp

app = Flask(__name__)
app.secret_key = 'book_shop'

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(sign_up_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(about_bp)
app.register_blueprint(search_bp)


if __name__ == "__main__":
    app.run(debug=True)

    