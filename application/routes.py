from application import app, db
from flask import render_template, request, Response, redirect, flash
import json
import sqlite3
from flask import g
from application.forms import LoginForm, RegisterForm
from application import models

DATABASE = 'testdb1.db'
connection = sqlite3.connect(DATABASE, check_same_thread=False)
cursor = connection.cursor()

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        first_name_and_password = cursor.execute(f"select first_name, password from User where email == \"{email}\"").fetchone()
        if first_name_and_password and models.User.check_password(first_name_and_password[1], password):
            flash(f"{first_name_and_password[0]}, you are successfully logged in!", "success")
            return redirect("/index")            
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", form=form, login=True)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = models.User(first_name, last_name, email, password)
        cursor.execute(user.get_sql_insert_command_for_user())
        connection.commit()
        flash("You are successfully registered!", "success")
        return redirect("/index")
    return render_template("register.html", form=form, register=True)
    
@app.route("/readpoem", methods=["GET", "POST"])
def readpoem():
#   cursor.execute("delete from Poem")
#   cursor.execute("delete from User")
#   
#   connection.commit()
#   cursor.execute(models.create_poem_table())
#   connection.commit()
#   poem = models.Poem("Margaret Atwood", "February", "Winter. Time to eat fat \n and watch hockey. In the pewter mornings, the cat, \n a black fur sausage with yellow \n Houdini eyes, jumps up on the bed and tries")
#   cursor.execute(poem.get_sql_insert_command_for_poem())
#   poem2 = models.Poem("Eleonor Farjeon", "Cats sleep anywhere", "Fitted in a cardboard box, \n In the cupboard with your frocks \n Anywhere! They don’t care! Cats sleep anywhere!")
#   cursor.execute(poem2.get_sql_insert_command_for_poem())
#   connection.commit()
    author = request.form.get('author')
    title = request.form.get('title')
    content = cursor.execute(f"select content from Poem where author = \"{author}\" and title = \"{title}\"").fetchone()
    
    return render_template("readpoem.html", data={"author": author, "title": title, 'content': content[0].split('\n')})


@app.route("/api/")
@app.route("/api/<id>")
def api(id=None):
    if id == None:
        jdata = poemsData
    else:
        jdata = poemsData[id]
    return Response(json.dumps(jdata), mimetype="application/json") 

#class User(db.Document):
#   id = db.IntField( unique=True )
#   name =  db.StringField( max_length=50 )
#
@app.route("/user")
def user():
#   User(id=11, name='Bett').save()
#   User(id=3, name='Gergo').save()
#   users = User.objects.all()
#   cursor.execute(models.create_user_table())
#   cursor.execute(models.insert_to_user())
#   connection.commit()
#   connection.close()
    
    return render_template("user.html", users=[{'id':1, 'name':'Boro'}, {'id':2, 'name':"Felcsi"}])