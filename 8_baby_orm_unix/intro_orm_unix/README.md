# ORM and Unix Introduction

### Learning Objectives
***Students Will Be Able To***

* Wrap SQL queries inside Python objects to make an ORM

---
### Context

* When working with back end technologies many frameworks come with a short hand so there's no need to write out SQL code from scratch. 

---
### Lesson

##### Part 1 - What is an ORM

* ORM stands for Object Relational Mapper. 
* This is a term for a programming practice where we can convert a type system to an object oriented language. 
* What does this mean in English?
* This means we will be wrapping our SQL queries into Python methods. Now the rows in a table can be instances of a class. 
* As mentioned in the Context of this lesson, many frameworks will have access to an "ORM" so the programmer does not have to write SQL queries from scratch.

***NOTE***

* Another example is the non relational database Mongo and it's (kind of)ORM framework Mongoose

##### Part 2 - ORM SELECT ALL SQL Example

* If you had an music application and wanted to search all artists in your database it may look something like 

```
SELECT * FROM Artists;
```
* Now using the ORM that you will build, you will just be invoking a method

```
Artists.all()
```
