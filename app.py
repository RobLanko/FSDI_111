#!/usr/bin/env python3
# -*- coding: utf8 -*-
# Flask Route definitions

from flask import Flask  # From flaskpackage import the flaskclass

app = Flask(__name__)  # initiate the flask class with parameter __name__

# app.route is a decorator that wraps the function underneath it


@app.route("/")
def index():  # view function that is being wrapped
    return "<h1>Hello World!</h1>"


@app.route("/about")
def about_me():
    me = {
        "active": True,
        "first_name": "Robert",
        "last_name": "Tulanko",
        "Hobbies": "Video Games"
    }
    return me
