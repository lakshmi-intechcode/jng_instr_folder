# Using External API's

### Learning Objectives
***Students will be able to...***

* Pull information from an external api
* Seed a database with information from an external api

---
### Context 

* Everything on the internet revolves around data. How do we grab it? Where can we get it? What can we do with it? 

---
### Lessons

##### Part 1 

* Everything that we've done so far has been about creating and manipulating our own database
* The database management isn't going to stop here
* We'll be taking it a step further by reaching out to other peoples databases and grabbing information from them


***NOTES***

* API
* REST
* CRUD
* HTTP VERBS
* JSON vs XML
* JSON Viewer
* Explain wrapper
* Explain Endpoints

##### Free APIs

* OMDB
* [Market On Demand API](http://dev.markitondemand.com/MODApis/) 

##### Resources

* [Andrew Havens Beginners Guide to Creating a REST API](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Miguel Grinberg Design a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)


# HOMEWORK IDEAS

* Use OMDB API
* Build a wrapper that will allow users to search for movies
* This wrapper will be imported to a models file
* The model will hold methods which will take in user input and pass that parameter to the wrapper file to make the request
* Once that is done build out a MVC application where the user can search a movie and the movie information will populate onto the terminal