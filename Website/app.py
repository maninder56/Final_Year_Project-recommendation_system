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
    return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)