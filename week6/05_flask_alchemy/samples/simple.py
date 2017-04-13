'''
alch1.py

A simple example of a web app using SQLAlchemy.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Define the path to your database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple.db'

# You can ignore this line if you want to. It suppresses a warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a database object from the SQLAlchemy class.
db = SQLAlchemy(app)

# Define your database table as a Python class.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

# Create instances of the User Class
    admin = User('admin', 'admin@example.com')
    kevin = User('kevin', 'kevin@ducks.com')

# Add these instances to the corresponding database table
    db.session.add(admin)
    db.session.add(kevin)

# Commit these changes
    db.session.commit()

# Examples of built in ORM methods to query for information
    print('query all users', User.query.all())
    print('filter for kevin', User.query.filter_by(username='kevin').first())





# This is pseudo code for how you might take data from the user through the browser
# parse the information and make a database query
# Depending on the database query you can choose to render template or send back JSON to the browser
# @app.route("/login", methods["POST"])
# def check_user():
#     username = request.form['username']
#     password = request.form['password']

#     is_user = User.query.filter_by(username = username, password = password)

#     if is_user != undefined:
#         return render_template('home.html', username = username)

