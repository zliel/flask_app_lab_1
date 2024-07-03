"""
Author: Zackary Liel
Class: CST205
Date: 7/3/2024
Abstract: This file is the root of the Flask application.
"""
# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return ('<p>Oscar A.: Iykyk</p>'
          '<p>Claire L.: Idk</p>'
          '<p>Kate S.: Tbh wdym</p>')

@app.route('/zackary')
def zackary():
    return render_template('template.html', acronym="Tfti", name='Zackary L.')