# Django Intro

### Learning Objectives
***Students will be able to...***

* How the internet works
* Install pip3 and Django
* Start a Django project and some apps
* Use basic regex commands

---

### Context

* Learn about the internet and how we can start putting things on it

---

### Lesson

##### Part 1 - What happens when I type Google.com into the browser and press enter?

* Request
* Response
* DNS

##### Part 2 - PIP Package Manager

***What is Pip***

* Pip is the package manager for Python
	* brew is the package manager for Macs
	* apt-get is the package manager for linux
	* npm is the package manager for node
	* and the list goes on
* We will be using `pip3` 
* pip3 is used as the package manager for python 3+

***Common Pip3 Commands***

* install pip3 - Everybody already has it
* install a package
	* `pip3 install name_of_package`
* upgrade a package
	* `pip3 install name_of_package --upgrade`
* uninstall a package
	* `pip3 uninstall name_of_package`
* view all packages installed
	* `pip3 freeze`
	* When working on a project you may see a `requirements.txt` file
	* This file will hold all the information of the kinds of packages a specific project is using
* Let's install virtual environment package and the newest version of django
* `pip3 install virtualenv`
* `pip3 install django` OR `pip3 install django==1.9`
	* if you leave off the version you will get the latest version
	* if you download an old version you can just upgrade that package

##### Part 3 - Starting Django / Code Along

***Common Commands***

* `django-admin.py startproject project_name`

***Start a project***

* Now lets start our own project. Make a folder called `blog` and cd inside of it
* use django to start the blog
* Start a project
	* `django-admin.py startproject blog`
* change directory into the blog and take a look at the files
	* `settings.py` - This file contains the settings for our application. We have such things as:
		* `import os` and `BASE_DIR`== Django creates certain paths dynamically for you to use depending on what operating system you are on and where your files are
		* `Installed Apps` - What are the default apps that Django comes with. When we make new apps we will have to include them here
			* `django.contrib.admin` - allows us to user the superuser admin page
			* `django.contrib.auth` - authentication for users 
			* `django.conf.urls` - we can use this with the `urls.py` folder
	* `urls.py` - The overall hub of all the urls you will have throughout building your project
	* `manage.py` - This file is used to call multiple commands in the terminal 
* Take a look at what you got so far
	* `python3 manage.py runserver`
	* `127.0.0.1:8000`

***Migrations***

* We have to make sure our database and django are all connected properly
* Using `manage.py` we can run a command called `migrate`
* `python3 manage.py makemigrations`
* `python3 manage.py migrate`

***Start an App***

* Apps vs Projects
	* Apps belong to a project
	* Projects contain multiple apps
* Apps are little components that build up the project as a whole
* Lets create an app for our project
	* `python3 manage.py startapp posts`
* posts is the name of our new app. 
* What files did we get with out new app
	* `admin.py` - don't touch for now
	* `tests.py` - don't touch for now
	* `models.py` - Just like the `Models in MVC pattern`
	* `views.py` - Help us organize what templates will be targeted during what request
	
***Using Models and Apps***

* We'll have to create a model class to use

```
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length =120)
	content = models.TextField()
	# updated will auto update 
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	# Timestamp will save and set one time
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	
	def __str__(self):
		return self.title
```

* Then we have to connect this app to the `settings.py` file

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]
``` 
* Whenever we make a new app we'll have to make migrations and migrate.
	* `python3 manage.py makemigrations` - tells django we made changes to our models
	* `python3 manage.py migrate` - tells django to apply those changes to our database
* There are many different fields you can utilize in the models
	* [Django Docs to see different Fields we can use in Models](https://docs.djangoproject.com/en/1.9/ref/models/fields/)
	
***CRUD / HTTP VERBS***

* Review all your knowledge
* CRUD
	* Create, Read, Update, Delete
	* Make new, Get, Edit, Delete
	* POST, GET, PUT/PATCH, DELETE

***Function Based Views***

* There are two types of views you will see in Django tutorials. They are Function Based Views and Class Based Views
* For today we will be looking at using Function Based Views and writing our views as functions
* `views.py` - is a file you will see in each of your apps
	* They do NOT hold templates or any html files
	* They take a request and turn it into a response
	* There are many ways to send a response
		* HttpResponse
		* render()
* Let's write a function that will return us something from the `views.py` file
* Import HttpResponse from django.http so we can send back a string

```
from django.http import HttpResponse
from django.shortcuts import render

def posts_home(request):

	return HttpResponse("<h1>HELLO WORLD</h1>")
```

***Request Response Cycle and `urls.py`***

* 


##### admin BONUS

1. Starting Project
	* Project Folder and files 
2. Start App
	* App folders and files
3. Project vs app
4. Intro url patterns --> Regex
5. Views.py - Take a request and turn it into a response
	* function based views 
5. HTML Forms 
	* actions
	* method 
	* What a form does
6. CRUD / HTTP VERBS
7. SQL reminder --> ORM


* ORM
* Objects is your DB manager
* Query through the manager object 
* all get filter
* query selectors in Django shell
	* make app
	* connect in settings installed app
	* make and migrate
	* import your Models 
* Manager object is a class attribute


* Regex Lesson

* Virtual env
	* make it `virtualenv env`
	* requirements.txt
		* `pip3 freeze`
		* copy that shit over
* Starting an app
* app vs project

* Views.py
	* Take a request and turn it into a response
* render creates a string of html. rend wraps a type of http response
	* httpresponseredirect
* settings.py
* urls.py
* admin.py

* HTML FORMS GET / POST 
* HTTP VERBS


* [Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)  





















