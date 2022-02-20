from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)

@app.route("/poems")
def poems():
    return render_template("poems.html")

@app.route("/login")
def login():
    return render_template("TO DO")

@app.route("/register")
def register():
    return render_template("TO DO")

