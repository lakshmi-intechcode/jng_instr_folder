# Parking Lot

## Description

The information in this markdown is intended to expand on your questions we were not able to cover during lecture periods. It will also include best practices on how to approach programming. 

---

## Lecture Parking Lot

#### Open your file into the Python REPL

* Using `-i` to run your file. If you have a python file that you normally run with `python3 file.py` you can use `-i` with it. This will open the interactive pyton3 repl with your file. 
* Below is an example where I made a file with a function to print a string. 
* I do not invoke that function inside of the file
* Make a file called `hello.py`

```
def hello():
	print("HELLO WORLD")
```
* Now save it and go back to the terminal
* Run the following command to open the file in the REPL
	* `python3 -i hello.py`
* Now you can do what you want with the file in the REPL. 
* Let's invoke the function

```
>>> hello()
>>> 'HELLO WORLD'
```

#### WHAT IS THE MAP.MIN FILE IN BOOTSTRAP

* In class we talked about the bootstrap map.min file
	* It is something that allows people to use bootstrap with css preprocessor such as LESS and SASS
* For the purposes of this class we don't have to go in depth about this topic

#### DJANGO STATIC FILES

* `Static Files` are your:
	* images
	* CSS Stylesheets
	* JavaScript Files
* [static folder documentation](https://docs.djangoproject.com/en/1.8/howto/static-files/)
* Your `settings.py` file will have to be changed to include the static files
* Put the following code at the very bottom of your `settings.py` file under `STATIC_URL`

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), 
    '/var/www/static/',
)
```
* os.path.join and Base_dir allow our application to be more dynamic with compatibility between different operating systems. 
	* A path on Linux may be different than Mac
* We are telling django to combine your static folder with the base directory
* Now we can incorporate our css stylesheets into our base html

***STEPS***

* Make a folder called `static` inside your project.
* Make a `style.css` file inside that `static` folder
* Open the css file and put in some CSS. `h1{color:red;}`
* Go into your base.html file and put the following

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" href="{% static "css/base.css" %}">
	<meta charset="UTF-8">
	<title>{% block head_title %}TRY DJ 1.9{% endblock head_title%}</title>
</head>
```
* Now your h1 tags should appear red

---

## Jason's Best Practices

* `Version Control` - Always push working code to github. Do not wait until you have "completed" the exercise. Version Control is meant to SAVE your progress. You wouldn't write a novel on microsoft word and only save it when the novel is done. 
* `Pseudo Code` - Think about your application before you start to code anything. Pseudo code what your objects will look like. Also make sure to write as many user stories as possible, and build out a detailed ERD if you are utilizing a database
* `DO NOT copy old code from a previous assignment.` If you want to use an old assignment for reference that's fine, but type out EVERYTHING. Repeat, Practice, Memorize.
* `DO NOT use code you don't understand.` If you decide to copy something you found through your research such as Stack Overflow answers, make sure you understand every letter of that code before using it. 
* `Doc Strings` - Use doc strings to comment out your code. They can also be viewed in the terminal when you `dir()` and `help()` your file. Doc strings can also be used to type out formatted print statements so there's no need to use string commands such as `\n`

---

## Resources

***Git / Github***

* [Github Ignoring Files](https://help.github.com/articles/ignoring-files/)

***Online Resources***

* [Trello Project Manager Web App](https://trello.com/)

***Database***

* [Database Normalization Wiki](https://en.wikipedia.org/wiki/Database_normalization)
* [Database SQl Index](http://www.programmerinterview.com/index.php/database-sql/what-is-an-index/)

***REST / CRUD / MVC***

* [HTTP Requests](http://www.tutorialspoint.com/http/http_requests.htm)
* [REST API Tutorial](http://www.restapitutorial.com/lessons/restfulresourcenaming.html)
* [Beginners Guide to Creating a REST API by Andrew Havens](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Designing a RESTful API with Python and Flask by Miguel Grinberg](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [URI Wiki](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)
* [REST Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer#Uniform_interface)

***JavaScript***

* [JavaScript is Sexy Callback Functions](http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/)
* [JavaScript is Sexy Scope and Hoisting](http://javascriptissexy.com/javascript-variable-scope-and-hoisting-explained/)
* [JavaScript is Sexy "this"](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/)
- [JavaScript is Sexy "call" / "bind" methods](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/)
* [AJAX Blog Explain](http://www.seguetech.com/blog/2013/03/12/what-is-ajax-and-where-is-it-used-in-technology)
* [AJAX on Tutorials Point (eh okay reading)](http://www.tutorialspoint.com/ajax/index.htm)
* [AJAX on jQuery.com, click through the links on the bottom](https://learn.jquery.com/ajax/)

***Python***

* [Python Tips Args and Kwargs](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python File IO Tutorials Point](http://www.tutorialspoint.com/python/python_files_io.htm)
* [What are Generators](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
* [Python @classmethods and @staticmethods](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner)
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
* [CSS Diner Exercise Tutorial](http://flukeout.github.io/)
* [CSS Pro Tips](https://github.com/AllThingsSmitty/css-protips)

***Django***

* [Stack OverFlow Answer has some Videos for Class Based Views](http://stackoverflow.com/questions/17414622/django-a-good-tutorial-for-class-based-views)

***Bash Commands***

* [Quick read about what is curl](https://quickleft.com/blog/command-line-tutorials-curl/)
- [Stack Overflow example of curl in use](http://superuser.com/questions/149329/what-is-the-curl-command-line-syntax-to-do-a-post-request)

***OAuth Resources***

- [Check out OAuth on wikipedia for a more "technical" explanation](https://en.wikipedia.org/wiki/OAuth)
- [Here's a list of OAuth Providers](https://en.wikipedia.org/wiki/List_of_OAuth_providers)

---

## Schedule 


| Weeks | Day 1                                                                 | Day 2                                                                              | Day 3                                                                   | Day 4                                        | Day 5                                    | Weekend Assignments                     |
|-------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------|------------------------------------------|-----------------------------------------|
| 1     | Python  Fundamentals  One                                             | Python Fundamentals Two                                                            | Intro To Object Oriented Programming                                    | More OOPS and Inheritance                    | Review                                   |                                         |
| 2     | Binary Search Linear Search Linked List                               | Bubble Sort Insertion Sort Stacks and Queues                                       | SQL Intro SQL CRUD MVC Intro Views /Models                              | SQL / MVC Models SQL Conn Createdb           | Binary Search Tree Merge Sort Quick Sort | Xmas Break RPG Blackjack                |
| 3     | SQL Relational DB SQL Foreign Keys                                    | SQL Relational DB SQL Joins                                                        | OMDB API                                                                | Markit API                                   | API                                      | Trader to Bank                          |
| 4     | Advanced Python Generators List Comprehensions Args and Kwargs        | Baby ORM Read                                                                      | Baby ORM  Full CRUD                                                     | Baby ORM  Full CRUD                          | Assessment                               | Pre Phase 2 Readings                    |
| 5     | Intro to  HTML vs HTML 5 CSS JS Syntax Diff                           | JS Scope Callbacks Closures Higher Order Functions DOM  DOM Events                 | jQuery Intro CDNs jQuery DOM                                            | CSS Positioning JavaScript THIS  Tic Tac Toe | Tic Tac Toe                              | Tic Tac Toe                             |
| 6     |  CSS Media Queries CSS Pseudo ClassesCSS Grids CSS Reset vs Normalize | Django Intro Pip Function Based Views HTML Forms Request Response Cycle Django ORM | URL Namespace Django Models Django Requests                             | Django Model Forms                           | WEEKEND PROMPT  UserLess Blog            | UserLess Blog                           |
| 7     | Django User Sessions Class Based Views                                | Homework Day                                                                       | Django Custom Validation Django Default Validators Debugging Assignment | Django as an API                             | AJAX                                     | Todo API  Todo Front End  Consuming API |
| 8     | Hacker News                                                           | Hacker News                                                                        | Hacker News                                                             | Review                                       | Assessment                               | OAuth                                   |

---

## How to find out if a number is divisible by another number (Found on Reddits YSK)

#### Obvious:

* 1 - Always.
* 2 - If the number is even.
* 5 - If the number ends in 5 or 0.
* 10 - If the numbers ends in 0.

#### Less Obvious:

* 3 - Add all of the digits in the number. If the result is divisible by 3, then so is the original number. (Note that this rule can be repeated with the result if you still don't know.)
* 4 - If the last 2 digits of the number are divisible by 4, then so is the entire number. If you don't know then halve the last 2 digits twice. If you still have a whole number then it is divisible by 4.
* 6 - If the number passes the '2' rule and the '3' rule, then, yes.
* 8 - If the last 3 digits of the number are divisible by 8, then so is the entire number. If you don't know then halve the last 3 digits three times. If you still have a whole number then it is divisible by 8.
* 9 - Add all of the digits in the number. If the result is divisible by 9, then so is the original number. (Note that this rule can be repeated with the result if you still don't know.)

#### Obscure:

* 7 - Remove the last digit from the number. Take the number formed by the remaining digits and subtract by 2x the removed digit. If the result is divisible by 7, then so is the original number.
* Example (889): 88-(9x2) = 88-18 = 70
=> 889 is divisible by 7.