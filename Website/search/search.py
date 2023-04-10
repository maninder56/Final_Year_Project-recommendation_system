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

from recomender import recomender


search_bp = Blueprint("search", __name__,
                  template_folder="templates")

@search_bp.route("/search", methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
      return do_search(request.form['searched'])
   else:
      return render_template('search.html')

# for testing 
reco = ["Lightning", "False Memory", "The Jester", "All Around the Town"]
reco = tuple(reco)

def do_search(title):
   try:
      # get recomended books 
      colloborative_filtering = recomender.recommend(title)
      colloborative_filtering = tuple(colloborative_filtering)

      query = f"""SELECT * FROM filtering_book_data WHERE "Book-Title" = "{title}" LIMIT 3;"""
      query2 = f"""SELECT * FROM filtering_book_data WHERE "Book-Title" In {colloborative_filtering} LIMIT 5;"""
      book = run_query.run_query(query)
      recommend_books = run_query.run_query(query2)
      if book[0] != None:
         return render_template('search.html',searched_book=book, recommend=recommend_books)
      
   except Exception as e:
      print(e)
   
   return render_template('search.html',book_not_found="Sorry, searched book is not available")
   