# Django Intro PART DOS

### Learning Objectives
***Students will be able to...***

* Using url template tags
* Making django orm relations (Creation/Access)
* Using Request Object to Obtain Form Data
---

### Context

* Continuing to become Full Stack Developers

---

### Lesson

##### Part 1 - URLS In Depth

* Yesterday we placed all our urls in the `project/urls.py` file
* Now we will be looking at how to organize our urls to include endpoints specific to our application.
* Let's start by making a `urls.py` file inside our app
	* Show off our post/blog app
	* Our `app/urls.py` file will contain urls that may look like this
	
```
urlpatterns = [
	url(r'^create$', views.create, name="create"),
]
```
* The url function can be broken down into the following parameters
	* `url( <pattern>, <view function>, name="<url alias>")`
* Now we'll have to chang what the `projects/urls.py` file will say

```
from django.conf.urls import include, url

urlpatterns =[
	url(r'^todos/', include("todos.urls", namespace="todos")),
]
```
* There is a function called include in this example that has the following syntax
	* `include(<app/urls>,namespace="<name of url file>")`
* notice we had to import the `include` function from `django.conf.urls`
* include allows us to connect to all the urlpatterns in a specific app, it will take in two arguments
	* the first argument will be the app url location
	* the second argument is what will be the `namespace` that will indicate those application urls are being targeted


***Why go through all this trouble***

* It is important to organize your urls so we do not have anything overlap as our projects grow in size.
* Imagine a project for a blog
	* You may have several apps
		* posts
		* comments
		* users
	* Each of these apps have their own create url pattern and create view
	* We want to be able to use the name create because it's very descriptive
	* We give each app url pattern a namespace so Django doesn't get confused when we want to create something

***redirect and template***

* We can also utilize `namespace:name` in a redirect function or a url template tag
* redirect function
	* Find example in post blog app
* url template tag
	* `{% url 'namespace:name' %}`


##### Part 2 - DJANGO REQUESTS

***Five Min Exercise***

* open up the deaf grandpa app and print out the requests in the HTML form
* Lets talk about this for a few minutes

***Pseudo explain***

* wsgi - The thing that's listening for requests. Turns it into a python object and send it django project
* This object will contain the request information
* request.POST is a variable inside this wsgi object. (The information from the body when a form with method POST is sent)
* The querystring is placed in the request.GET attribute. 

##### Part 3 - Models Take Two

***Five Min Exercise***

* Go to the whiteboard and diagram the different DB relationships
* How might you represent membership? (pick one of the three examples or come up with your own)
	* membership to a gym
	* membership to a club
	* membership to a store

***Lesson Continue***

* Review of Database Relations
	* One to One
	* One to Many
	* Many to Many
* How do you represent membership?
* Django ORM has magic
	* Django Foreign key
	* Django has the ability to inverse lookup a relation
* Django Docs Tutorial, look at fields that will help with
	* Many to Many
	* One to Many / Foreign Key














## Shit to know

* MORE ORM STUFF
	* One to Many Relationships
	* How do you set up multiple tables
	* Reverse something
	* Build your schema using Django Models
	* 1 App with two models. connect them in the models file
		* models.foreignkey takes parameter, it will be the class of the other model.
		* This shit figures out the id of the other table by itself

```
class Employee(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()

class Department(models.Model):
    name = models.CharField(max_length=30)
    budget = models.DecimalField(max_digits=15,decimal_places=2)
    employees = models.ManyToManyField(Employee)

class Manager(models.Model):
    employee = models.ForeignKey(Employee)

class Team(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(Manager)
    employees = models.ManyToManyField(Employee)
```
* Look through the Django Docs to find out how to do this
	* Many To Many
	* One To Many / Foreign Key
	* DecimalField
* Reverse manager 

* Teach url template tags in forms
* url template tags
* continue HTML forms
* name spacing urls
* app urls vs project urls


======================


#### The Database Model

- Make a todo model that holds a todo **`objective`**, `created_at`, and `completed` for a todo with the appropriate model fields.
- Make your migrations, migrate your db, and run your server.

#### URLS/Routes

Check out our **two** `urls.py` files: 
- `project/urls.py` routes all requests to `/todos` 
- `todos/urls.py` file in the todos app. 

* Yesterday we placed all of our urls in the `project/urls.py` file
* Now we will be looking at how to organize our urls to include app specific endpoints
* We will have to make a urls.py file in the app folder. In this example it will be in the todos folder
* app/urls also known as the `todos/urls.py` will have their patterns look like this:

```
urlpatterns = [
	url(r'^create$', views.create, name="create"),
]
```
* `project/urls.py` will look similar to the code below

```
from django.conf.urls import include, url

urlpatterns =[
	url(r'^todos/', include("todos.urls", namespace="todos")),
]
```


The todos/urls.py file is pure Python code and is a simple mapping between URL patterns (regular expressions) to Django Views (Functions/Classes). Separating our urls into project/urls and app/urls keeps our app modular. 

#### Create

* Make a new route in your todos url file. 
* The urlpattern will be `create`
* It will follow the below syntax
	* `url(r'^create$', views.create, name="create"),`	
* url function takes two required positional arguments. We can pass it a third argument that will alias the url. (using the "name" keyword argument)
* The first parameter is the url regular expression that will match the incoming path
* The second parameter will target a view function
* Your form on `index.html` should look something like this:
```html
<form action="urltemplatetag" method="POST">
	{% csrf_token %}
	<input name="name" type="text">
	...
</form>
```
* Keep in mind that depending on the request.method (i.e. GET or POST). Our function based view for create will either render the `todo` form if a GET request is sent as opposed to the creation of a `todo` if a POST is sent. The POST route should save the todo and redirect back to the main page.

#### Read
Now that you're able to create new `todo` objects. We will need to be able to render a given `todo` objects' on it's own page as well as a list of ALL `todo` objects. To do this, you'll need to write code in the respective template and the view function to show a list of all the todos. Make every todo a link to a new page that displays their information. Go back to [Django docs on URLs](https://docs.djangoproject.com/en/dev/topics/http/urls/#named-groups) and read about Named Groups.You will need to use these in order to do your database look up for a `todo`.

It should look something like this (Make sure you know what this regex is doing!): 
```py
url(r'^(?P<todo_id>[0-9]+)/$', views.todo),
```

Your `index.html` should look something like this:
```html
{% for todo in todos %}
	<p>{{ todo.name }}</p>
{% endfor %}
```
#### Update

Now we are going to make an update route that takes the todo info and pre-populates a form with the `todo` information. You're going to want to load the `todo` information from the database, pass it to the template, and render your update form _with_ the information.

In the template, you're going to want something like:
```html
<form name="todos" action="/update" method="POST">
	{% csrf_token %}
	<input name="name" type="text" value="{{todo.name}}">
	...
</form>
```
On submit, update the `todo` and redirect to the `todo` objects' individual page (i.e. your READ route). Put a link to this route on the index page next to each todo or on the todo's individual page.

#### Delete

Finally, make a route that deletes a `todo` from the database. You don't really need a new page for this - just a route and a redirect. Put the link on the `todo` objects' individual page.

#### Bonus - the Admin

After you've created a few todos, follow this bit of the [Django Tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) and connect to your built in admin backend. This is one of the best built-in features of Django that definitely makes your life a little easier (i.e. It does all your CRUD ;) ). Play around and take a look at its functionality.


>>>>>>>>>>>>>>>>>>>>>>base







