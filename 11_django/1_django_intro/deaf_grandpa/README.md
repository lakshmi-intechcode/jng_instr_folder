# Deaf Grandpa

##### Description

* Welcome to your first attempt at web development. Say hi to your deaf old Grandpa! 
* Well, don't say *'hi'*. Say *'HI GRANDPA'*. He can't hear so well.
* You have been provided with some starter code. 
* If you enter your phrase in lower case your Grandpa will respond with *'What, I can't hear you Sonny!*
* If you enter your phrase in upper case, he should repeat what you said and then insult you with something funny.
* Make sure to run your server and test your code in action
	* `python3 manage.py runserver`
	* 127.0.0.1:8000

##### Objectives

***The Main Page***

* Your starter code has a form built out for you
* You will need to extend it so grandpa will say something back
* Remember there are three parts to this page
	* 

The "View": In Django, controller functions are called "views". It makes sense, because they control which variables and data the user gets to see in the template. You'll find this in `deafgrandpa/views.py`

The "Template": This is the .html file that is rendered on the page. It can be sent a dictionary from the view when rendered. You'll find this in `deafgrandpa/templates/deafgrandpa/*.html`

The URL dispatch: This is where the routing is done - it receives requests and tries to match the urls using regex. Take a look at `deafgrandpa/urls.py`

#### The Form Submission

If you look at the form, it has an action and a method. The action is `/say`, and the method is POST. So we will need to post data to `/say`.

Create a route in urls.py that will go to `/say`, and create the corresponding function in `views.py`.

All view functions take the request as an argument. It holds a lot of data about the user and their actions - do some sandboxing.

You will find the data the user sent in a dictionary stored at `request.POST`.

We don't want to render on a POST route - we want to redirect back to a GET. POSTs are only for sending data to server - GETs are for retrieving. [Read more about GET and POST](http://www.w3schools.com/tags/ref_httpmethods.asp).

So redirect back to the index route, with a [query string](http://en.wikipedia.org/wiki/Query_string) attached. Something like:
```
return redirect('/?grandpasays=I can't hear you Sonny!')
```
#### Back to the Main Page

Figure out how to get the contents of this query string and pass it into the rendered template. You will find resources on render and redirect below. The Django documentation is less accessible than we would all like, so read carefully.

#### Resources

[Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)  
[Writing Views](https://docs.djangoproject.com/en/stable/topics/http/views/)  
[Django Forms API](https://docs.djangoproject.com/en/stable/ref/forms/api/)  
[Render and Redirect](https://docs.djangoproject.com/en/stable/topics/http/shortcuts/)
