from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False, index=True)

@app.route("/poems")
def poems():
    return render_template("poems.html", poemsData=[{"author":"Margaret Atwood", "title":"February"}, {"author":"Eleonor Farjeon", "title":"Cats sleep anywhere"}], poems=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)
    
    