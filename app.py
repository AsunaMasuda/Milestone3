import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value generated via secrets python module.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/fundamentals')
def show_fundamentals():
    return render_template('fundamentals.html', fundamentals=mongo.db.fundamental_movements.find())


@app.route('/public-sessions')
def show_public_sessions():
    return render_template('public-sessions.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/create-session')
def create_session():
    return render_template('create-session.html')


@app.route('/my-sessions')
def my_sessions():
    return render_template('my-sessions.html')


@app.route('/session-view')
def session_view():
    return render_template('session-view.html')


@app.route('/edit-session')
def edit_session():
    return render_template('edit-session.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)