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
* This can be called at any time a user wants to search for ALL artists
* How might we do this if we wanted to actually have some where conditions? return a specific value?

```
SELECT * FROM Artists WHERE name = "Linkin Park";
```
* With an ORM this may look like

```
Artists.filter(name = "Linkin Park")
```
* What if we had multiple conditions? What can we use for that? (**Kwargs)

##### Resources - Things for Homework

* `setattr()` - This is used to set an attribute to an instance of a class. It takes in three parameters. The class name, the attribute name, and the value. How might you use this with kwargs? 
* `hasattr()` - This will check for an attribute in a instance. It will take in two parameters. The name of the class and the property you're looking for
	* If you see documentation for `getattr()` we suggest using hasattr over that because getattr can return an error and make it seem like it does not exists at all. 
* [Blog for setattr and hasattr](http://www.dotnetperls.com/type-python)
* `class.__name__` - This is used to get our class name as a string
* Check out this [stack overflow answer](http://stackoverflow.com/questions/18326719/python-class-variable-name-vs-name) for `__name__` 
* `**kwargs` - we already studied this. Keyword arguments!!! wooooo