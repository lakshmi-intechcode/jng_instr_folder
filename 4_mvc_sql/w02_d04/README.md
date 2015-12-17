# Python3: SQLite3 and MVC's

### Learning Objectives

* Connect a sqlite3 database to a python file
* Open and close connections to a database from a py file
* Build and import a seed file for testing data/code

---

### Context

* Yesterday we learned basic SQL CRUD commands. Now lets utilize these to help us keep persistent data.
* Along side persistent data, well complete our MVC application.

---

### Lesson

* Show them how to make a create file
* Show them how to make a seed file
* Show them how to connect to database
* Show them how to grab and return values from a database
* Python sqlite3 module commands
	* sqlite3 comes shipped with every version of python after 2.5 so we can just import it. We do not need to go and download it. 
	* sqlite3.connect
	* connect.cursor
	* cursor.execute
	* connect.execute
	* connect.commit
	* connect.close
	* cursor.fetchall
* Data sanitization


#### Part 1 - Recap of Yesterday and how does SQLite fall into our MVC app

* The concept of MVC is to write organized code
* Yesterday we worked on connecting two separate files. Each file with their specified purpose. `Views` and `Controllers`
* As we know the `Controller` holds the application logic so it not only talks to the view but also talks to the `Models` which interacts with the database

***Five Min Exercise***

* Draw the MVC diagram. Go from the browser to the database to the view

* Make a table for the CRUD operations and their translation to SQL syntax


#### Part 2 - Createdb.py

* Alright now we're going to make a file to create our database. 
* Yesterday we practiced all our SQL CRUD commands in the terminal
* Now we're going to import the sqlite3 module into a python file for use.

```
import sqlite3

conn = sqlite3.connect('databasename.db')

conn.execute(
	"""
	CREATE TABLE tablename (
		id INTEGER PRIMARY KEY, 
		character TEXT,
		movie TEXT,
		year INTEGER
	)
	"""
)

conn.commit()
conn.close()

print("Your database was created")
```
* `.connect("dbname.db")` allows us to connect to a database. 
	* If there is no database with that name, this command will automatically make one
	* We assign this connection to a variable called `conn` which we will use later
* `conn.execute` - we use the execute method from the sqlite3 module to run a SQL command in python. 
* `conn.close` will close the connection to the database
* The last print statement is there to give you some notification that everything ran smoothly. 

***Five Min Exercise***

* create a createdb file
* Don't actually write code. just pseudo code. 
* What will you need to create to ensure your database has all the information you want for you rpg game?
* At the end well come back and review what you have. I don't want incomplete databases being made, then they have to be deleted and remade, yatta yatta. 


#### Part 3 - Seed.py

* So before we move over to our Models lets actually put something in our database that we can use to test. 
* This is called a seed file
* We only have to run this file ONCE when the data base is created
* This file is separate from our createdb.py file for organizational purposes

```
"""
Seed your database with admins
"""

import sqlite3

db = 'mydb'

USERS = [
	["Anna Kendrick", "soulmate", "12345", "mylove@myheart.com", "[1234567,1234567,23455647]"],
	["Peter Parker", "spiderman", "12345", "parker@parker.com", "[1234563,23451234,234567]"]
]

conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM user")

for user in USERS:
	c.execute("""
		INSERT INTO user ("name", "username", "password", "email", "phone_num") VALUES (?, ?, ?, ?, ?)""",(user[0], user[1], user[2], user[3], user[4]))

conn.commit()

c.close()

print("Looks like we're all good")
```
* `.cursor()` 
* `.commit()` - You only use this on the manipulation of data in your DB
* `.close()` - closing your connection

#### Part 4 - Models

* Now time for actually talking to the Models
* Let's start slow and look at how we can use SQL Commands in the py file

```
import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()
```
* Great it looks fairly simple
* Notice we didn't use `.commit` because we did not manipulate any DB information
* This looks great but how can we actually write our code to run queries only at certain points, and also return what was found. 
* Same way we've been writing the Views and the Controllers

```
import sqlite3

class Classname:

	def __init__(self, x, y, z):
		blah blah blah
	
	def create_login(self,username, password):
		conn = sqlite3.connect('databasename.db')
		c = conn.cursor()
		
		the_variable = c.execute(
			"""
			SQL COMMAND HERE. (INSERT INTO tablename blah blah)
			"""
		)
		
		return the_variable.fetchall()
```



#### Part 5 - Sanitize Data - fix this. move it up


#### Resources

* [SQLite3 Python Tutorials Point](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
* Use dir() to look at the various methods that the sqlite3 module gives you
* [The Python3 SQLite docs](https://docs.python.org/3.4/library/sqlite3.html)