# Flask Microframework

### Learning Objectives
***Students will be able to...***

* Diagram the request response cycle
* Set up a Flask server
* Send data as JSON from a Flask server

---
### Context

* We are going to be Full Stack Web Developers

---

### Lesson

##### Part 1 - What Is Flask? Why do we need it?

* [Flask](http://flask.pocoo.org/) is a microframework written in Python.
* A microframework is a web application framework that prioritizes
speed, simplicity, and flexibility. Microframeworks are commonly used
to serve APIs and simple web applications. These days, they're also
commonly used to serve everything else.
* Every web application framework, in every language, manages the
following concepts:
	* routes
	* a request object
	* HTTP responses with HTML templates
	* JSON responses
	* object relational mapping
	* sessions
* Today in particular, we'll cover *routes*, *JSON* responses, and the
*request* object.

##### Part 2 - Routes

* A route is just a URL path -- the extra bit after `http://mywebsite.com`.
* It's not more than that, but every framework has a way to define what *routes*, or URLs, it responds to.
* In Flask, that way is a [decorator](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html)
called `@app.route()`.

##### Part 3 - Sending JSON with Flask

* `JSON` - [JavaScript Object Notation](https://tools.ietf.org/html/rfc7159) is a specific kind of format data will be sent as. Very similar to dictionaries in Python
* To send a JSON response from Flask, use the function `jsonify()`.
* Congratulations, you've just built an API!

##### Part 4 - Request Object

* The *request object* is built from the [HTTP header](https://tools.ietf.org/html/rfc7230) of a request. 
* Every HTTP request and response has a header containing metadata, such as the
*method* of request (GET or POST), session data, query string
arguments, and form data.
* Flask stores request data in an object called `request`.
