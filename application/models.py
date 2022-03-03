import flask
from werkzeug.security import generate_password_hash, check_password_hash

class User():

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        
    @classmethod
    def check_password(cls, hassed_password, password):
        return check_password_hash(hassed_password, password)    

    def get_sql_insert_command_for_user(self):
        return f'''INSERT INTO User (first_name, last_name, email, password)
                                VALUES (\"{self.first_name}\", \"{self.last_name}\", \"{self.email}\", \"{self.password}\")'''
        
        
class Poem():
    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content

    def get_sql_insert_command_for_poem(self):
        return f'''INSERT INTO Poem (author, title, content)
                                VALUES (\"{self.author}\", \"{self.title}\", \"{self.content}\")'''
                                
    

class Like():
    email = ""
    author = ""
    title = ""


def create_user_table():
    return '''CREATE TABLE User (
        first_name varchar(50) NOT NULL,
        last_name varchar(50),
        email varchar(50) NOT NULL UNIQUE,
        password varchar(15)
     );'''

def create_poem_table():
    return '''CREATE TABLE IF NOT EXISTS Poem (
        author varchar(50) NOT NULL,
        title varchar(50) NOT NULL,
        content varchar(50) NOT NULL
     );'''
    
                        