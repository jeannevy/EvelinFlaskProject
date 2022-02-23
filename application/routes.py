from application import app
from flask import render_template, request, Response 
import json

poemsData = [{"author":"Margaret Atwood", "title":"February"}, {"author":"Eleonor Farjeon", "title":"Cats sleep anywhere"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False, index=True)

@app.route("/poems/")
@app.route("/poems/<century>")

def poems(century="20th"):
    return render_template("poems.html", poemsData=poemsData, poems=True, century=century)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)
    
@app.route("/readpoem", methods=["GET", "POST"])
def readpoem():
    author = request.form.get('author')
    title = request.form.get('title')
    return render_template("readpoem.html", data={"author": author, "title": title})


@app.route("/api/")
@app.route("/api/<id>")
def api(id=None):
    if id == None:
        jdata = poemsData
    else:
        jdata = poemsData[id]
    return Response(json.dumps(jdata), mimetype="application/json") 

