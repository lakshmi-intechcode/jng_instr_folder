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

##### Part 2 - AS and ORDER BY

* Let's make a createdb file

```
CREATE TABLE buildings(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  city TEXT,
  build_year INTEGER
);

CREATE TABLE residents(
  member_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  residents INTEGER
);
```

* Let's make a seed file


* Make a database with a Python file
* Make a Seed file to populate that database with two tables
* Show them the `AS` statement
* Show thme the `ORDER BY` statement

```
SELECT column, column_INT/number AS new_column_name FROM table ORDER BY new_column_name;
```


##### Part 3 - JOIN and INNER JOIN (Cross Join?)

