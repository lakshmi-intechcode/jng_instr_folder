# Parking Lot

## Description

The information in this markdown is intended to expand on your questions we were not able to cover during lecture periods. It will also include best practices on how to approach programming. 

---

## Lecture Parking Lot

* Using `-i` to run your file. If you have a python file that you normally run with `python3 file.py` you can use `-i` with it. This will open the interactive pyton3 repl with your file. Below is an example where I made a file with a function to print a string. I do not invoke that function inside of the file

```
//inside your terminal make a python file
touch hello.py

//inside hello.py

def hello():
	print("HELLO WORLD")
	
//Do not invoke it
//Back inside of your terminal

python3 -i hello.py

>>> hello()
>>> 'HELLO WORLD'
```
* In class we talked about the bootstrap map.min file
	* It is something that allows people to use bootstrap with css preprocessor such as LESS and SASS

***Django Static Files***

* Django static files are the CSS, JS, images, and the like that you will be incorporating into your project
* Take a look at the [static folder documentation](https://docs.djangoproject.com/en/1.8/howto/static-files/)
* If you want to include images, CSS, Javascript files, etc. You will need to change your `settings.py` file to include your defined static folder in the `STATICFILES_DIRS` tuple

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), //This joins your defined static folder with the base directory and adds it to the staticfiles_dir tuple
    '/var/www/static/',
)
```

* If we do it this way we can configure our urls in the `urls.py` file to look something like this: (This example takes into account an app with a todo model)   
    * todos/create/
    * todos/<todo_id>/
    - todos/<todo_id>/update/
    - todos/<todo_id>/delete/


---

## Jason's Best Practices

* `Version Control` - Always push working code to github. Do not wait until you have "completed" the exercise. Version Control is meant to SAVE your progress. You wouldn't write a novel on microsoft word and only save it when the novel is done. 
* `Pseudo Code` - Think about your application before you start to code anything. Pseudo code what your objects will look like. Also make sure to write as many user stories as possible, and build out a detailed ERD if you are utilizing a database
* `DO NOT copy old code from a previous assignment.` If you want to use an old assignment for reference that's fine, but type out EVERYTHING. Repeat, Practice, Memorize.
* `DO NOT use code you don't understand.` If you decide to copy something you found through your research such as Stack Overflow answers, make sure you understand every letter of that code before using it. 
* `Doc Strings` - Use doc strings to comment out your code. They can also be viewed in the terminal when you `dir()` and `help()` your file. Doc strings can also be used to type out formatted print statements so there's no need to use string commands such as `\n`

---

### Resources

***Some Online Resources***

* [Trello Project Manager Web App](https://trello.com/)

***Database***

* [Database Normalization Wiki](https://en.wikipedia.org/wiki/Database_normalization)
* [Database SQl Index](http://www.programmerinterview.com/index.php/database-sql/what-is-an-index/)

***REST / CRUD / MVC***

* [HTTP Requests](http://www.tutorialspoint.com/http/http_requests.htm)
* [Beginners Guide to Creating a REST API by Andrew Havens](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Designing a RESTful API with Python and Flask by Miguel Grinberg](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [URI Wiki](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)

***JavaScript***

* [JavaScript is Sexy Callback Functions](http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/)
* [JavaScript is Sexy Scope and Hoisting](http://javascriptissexy.com/javascript-variable-scope-and-hoisting-explained/)
* [JavaScript is Sexy "this"](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/)
- [JavaScript is Sexy "call" / "bind" methods](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/)

***Python***

* [Python Tips Args and Kwargs](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python File IO Tutorials Point](http://www.tutorialspoint.com/python/python_files_io.htm)
* [What are Generators](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
* [Why Class Methods Stack OverFlow 1](http://stackoverflow.com/questions/10586787/when-should-i-use-classmethod-and-when-def-methodself)
* [Why Class Methods Stack OverFlow 2](http://stackoverflow.com/questions/38238/what-are-class-methods-in-python-for)

***Design***

* [design theory by tutsplus](http://webdesign.tutsplus.com/categories/design-theory)

***How the Internet Works***

* [how dns works comic](https://howdns.works/episodes/)

***HTML and CSS***

* [What is Normal Document Flow](http://webdesign.tutsplus.com/articles/quick-tip-utilizing-normal-document-flow--webdesign-8199)
* [rem vs em?](https://j.eremy.net/confused-about-rem-and-em/)
* [What does auto really mean?](http://stackoverflow.com/questions/4471850/what-is-the-meaning-of-auto-value-in-a-css-property)
* [Positioning from vanseodesign](http://vanseodesign.com/css/css-positioning/)
* [Learn Layout DOT COM](http://learnlayout.com/)
* [CSS DINER EXERCISE TUTORIAL](http://flukeout.github.io/)





---

### Schedule 

| Weeks | Day 1                                                          | Day 2                                        | Day 3                                      | Day 4                              | Day 5                                    | Weekend Assignments      |
|-------|----------------------------------------------------------------|----------------------------------------------|--------------------------------------------|------------------------------------|------------------------------------------|--------------------------|
| 1     | Python  Fundamentals  One                                      | Python Fundamentals Two                      | Intro To Object Oriented Programming       | More OOPS and Inheritance          | Review                                   |                          |
| 2     | Binary Search Linear Search Linked List                        | Bubble Sort Insertion Sort Stacks and Queues | SQL Intro SQL CRUD MVC Intro Views /Models | SQL / MVC Models SQL Conn Createdb | Binary Search Tree Merge Sort Quick Sort | Xmas Break RPG Blackjack |
| 3     | SQL Relational DB SQL Foreign Keys                             | SQL Relational DB SQL Joins                  | OMDB API                                   | Markit API                         | API                                      | Trader to Bank           |
| 4     | Advanced Python Generators List Comprehensions Args and Kwargs | Baby ORM Read                                | Baby ORM  Full CRUD                        | Baby ORM  Full CRUD                | Assessment                               |                          |
|       |                                                                |                                              |                                            |                                    |                                          |                          |
|       |                                                                |                                              |                                            |                                    |                                          |                          |
|       |                                                                |                                              |                                            |                                    |                                          |                          |
|       |                                                                |                                              |                                            |                                    |                                          |                          |




---

### How to find out if a number is divisible by another number (Found on Reddits YSK)

##### Obvious:

* 1 - Always.
* 2 - If the number is even.
* 5 - If the number ends in 5 or 0.
* 10 - If the numbers ends in 0.

##### Less Obvious:

* 3 - Add all of the digits in the number. If the result is divisible by 3, then so is the original number. (Note that this rule can be repeated with the result if you still don't know.)
* 4 - If the last 2 digits of the number are divisible by 4, then so is the entire number. If you don't know then halve the last 2 digits twice. If you still have a whole number then it is divisible by 4.
* 6 - If the number passes the '2' rule and the '3' rule, then, yes.
* 8 - If the last 3 digits of the number are divisible by 8, then so is the entire number. If you don't know then halve the last 3 digits three times. If you still have a whole number then it is divisible by 8.
* 9 - Add all of the digits in the number. If the result is divisible by 9, then so is the original number. (Note that this rule can be repeated with the result if you still don't know.)

##### Obscure:

* 7 - Remove the last digit from the number. Take the number formed by the remaining digits and subtract by 2x the removed digit. If the result is divisible by 7, then so is the original number.
* Example (889): 88-(9x2) = 88-18 = 70
=> 889 is divisible by 7.