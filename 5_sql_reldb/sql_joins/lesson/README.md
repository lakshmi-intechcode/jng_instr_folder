# Relational DB's / SQL Joins

### Learning Objectives
***Students will be able to...***

* Make SQL JOIN queries to grab data from multiple tables

---
### Context

* Advanced SQL Queries that allow us to pull data from multiple tables all at once without making multiple queries

---
### Lesson

##### Part 1 - Multiple Tables / Database Normalization

* Remember the music example from the first day of SQL? Draw out your example
	* Three tables
	* Artists, Songs, Albums
* In the music example the table `Albums` would have the foreign keys to both the artists and songs tables. 

***Five Min Exercise***

* What are some pros and cons to having your database formatted this way? 

***Database Normalization***

* This ERD follows the principles of [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
* We are organizing our data to minimize redundancy
* It allows us to have more consistent data
* Normalizing a database involves taking one large table and breaking it up into smaller tables. 
* Then use foreign keys to reference each other.

***Example***

* With the music database above, if we had it all on one table (also known as a flat table) then we would have to update everything just to insert one item
* With multiple tables we may only have to edit the songs table if a artist comes out with a new song. Or the albums table if there's a new album that consists of songs that already exists in the database. 
* Less redundancies

***The One Bad Thing***

* We are using more memory to store all this data and build all these relationships

##### Part 2 - Exercise createdb / seed

***Five Min Exercise***

* Make a createdb file and a seed file. 
* createdb file will have
	* two tables: `buildings` `residents`
	* Buildings will have three columns: `name`, `city`, `build_year`
	* residents will have three columns: `first_name`, `last_name`, `rent`
	* which table should have the foriegn key? 
* seed your database with the following information

```
BUILDINGS =[
	["Empire State", "New York", 1930],
	["Bradbury", "Los Angeles", 1893],
	["White House", "Washington D.C.", 1800],
]

RESIDENTS = [
	["Jay", "Z", 100000],
	["Kobe", "Bryant", 90000],
	["Barack", "Obama", 50000],
]
```


---
***ANSWER***

CREATEDB FILE

```
import sqlite3

db = sqlite.connect('livingdb')

cursor = db.cursor()

cursor.execute('''
	CREATE TABLE buildings(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		city TEXT,
		build_year INTEGER
	);
''')

cursor.execute('''
	CREATE TABLE residents(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name TEXT,
		last_name TEXT,
		rent INTEGER,
		building_id INTEGER,
		FOREIGN KEY(building_id) REFERENCES buildings(id)
	);
''')

db.commit()
db.close()
```

SEED FILE

```
import sqlite3

db = 'livingdb'

BUILDINGS =[
	["Empire State", "New York", 1930],
	["Bradbury", "Los Angeles", 1893],
	["White House", "Washington D.C.", 1800],
]

RESIDENTS = [
	["Jay", "Z", 100000, 1],
	["Kobe", "Bryant", 90000, 2],
	["Barack", "Obama", 50000, 3],
]
conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM buildings")
c.execute("DELETE FROM residents")

for building in BUILDINGS:
	c.execute("""
		INSERT INTO buildings ("name", "city", "build_year") VALUES (?, ?, ?)""",(building[0], building[1], building[2]))

conn.commit()

for resident in RESIDENTS:
	c.execute("""
		INSERT INTO residents ("first_name", "last_name", "rent") VALUES (?, ?, ?)""",(resident[0], resident[1], resident[2]))

conn.commit()

c.close()
```


##### Part 3 - AS / ORDER BY / JOINS

* Now let's take the data from the two tables and order their results the way we want them. 
* We can even create a new column for this query's output
* Open up the database using sqlite3 in the terminal

```
SELECT residents.first_name, residents.last_name, buildings.city, residents.rent * 12 AS yearly_rent FROM residents, buildings ORDER BY yearly_rent;
```

##### Part 3 - JOIN and INNER JOIN

* Without knowing it we already performed a SQL Join
* A Join is performed whenever we have a relation, and join two or more tables to return a combined value/values
* Other syntax to do that would be this

```
SELECT residents.first_name, residents.last_name, buildings.city, buildings.name FROM residents INNER JOIN buildings;
```


* INNER JOIN is the most commonly used join. 
* There are others but for the purposes of this course we will not be exploring them




