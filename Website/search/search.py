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


search_bp = Blueprint("search", __name__,
                  template_folder="templates")

@search_bp.route("/search")
def search():
   return render_template('search.html')



