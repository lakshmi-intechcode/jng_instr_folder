Intro to CRUD
=============

In this challenge we're going to be building a classic **CRUD** app which simply lists some companies. In case you forgot, **CRUD** stands for: **C**reate - **R**ead - **U**pdate - **D**elete. These are the fundamental database functions that occur through most, if not all, web applications.


#### Resources:
- [Django Model Fields](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/ )
- [HTTP Methods for Restful Services](http://www.restapitutorial.com/lessons/httpmethods.html)
- [Anatomy of a URL](http://doepud.co.uk/blog/anatomy-of-a-url)
- [REST](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)

#### The Database Model

- Make a Company model that holds a company `name`, `phone number`, and `email address` for a company with the appropriate model fields.
- Make sure to include your Postgres settings in `settings.py` and to create the db.
- Make your migrations, migrate your db, and run your server.

#### URLS/Routes

Check out our **two** `urls.py` files: 
- `project/urls.py` routes all requests to `/companies` 
- `urls.py` file in the companies app. 

A clean, elegant URL scheme is an important detail in a high-quality Web application. Django lets you design URLs however you want, with no framework limitations. This module is pure Python code and is a simple mapping between URL patterns (simple regular expressions) to Python functions (your views). This separation allows our app(s) be entirely modular; we can take this app out of this project and put it in another one with minimal work.

#### Static Files (i.e. CSS, JS, Images, etc.)
Also take a look at the [static folder](https://docs.djangoproject.com/en/stable/howto/static-files/) and the link to the CSS file inside in our template. If you want to include images, CSS, Javascript files, etc. You will need to change your `settings.py` file to include your defined static folder in the `STATICFILES_DIRS` list:
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
```
`os.path.join(BASE_DIR, "static")` joins your defined static folder with the base directory and adds it to the staticfiles_dir list.  

Now that our Django app has been properly set up to include our static files and our inital `Company` model, let's begin creating our URls! You will need the following routes configured in your apps' `URLs.py` file:
   
    - companies/create/
    - companies/<company_id>/
    - companies/<company_id>/update/
    - companies/<company_id>/delete/


#### Create

Make a new route, `/create`, that has a form and will insert a new company into the database.
Your form on `index.html` should look something like this:
```html
<form name="companies" action="/create" method="POST">
	{% csrf_token %}
	<input name="name" type="text">
	...
</form>
```
Keep in mind that depending on the request.method (i.e. GET or POST). Our function based view for create will either render the `Company` form if a GET request is sent as opposed to the creation of a `Company` if a POST is sent. The POST route should save the company and redirect back to the main page.

#### Read
Now that you're able to create new `Company` objects. We will need to be able to render a given `Company` objects' on it's own page as well as a list of ALL `Company` objects. To do this, you'll need to write code in the respective template and the view function to show a list of all the companies. Make every company a link to a new page that displays their information. Go back to [Django docs on URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/#named-groups) and read about Named Groups.You will need to use these in order to do your database look up for a `Company`.

It should look something like this (Make sure you know what this regex is doing!): 
```py
url(r'^(?P<company_id>[0-9]+)/$', views.company),
```

Your `index.html` should look something like this:
```html
{% for company in companies %}
	<p>{{ company.name }}</p>
{% endfor %}
```
#### Update

Now we are going to make an update route that takes the company info and pre-populates a form with the `Company` information. You're going to want to load the `Company` information from the database, pass it to the template, and render your update form _with_ the information.

In the template, you're going to want something like:
```html
<form name="companies" action="/update" method="POST">
	{% csrf_token %}
	<input name="name" type="text" value="{{company.name}}">
	...
</form>
```
On submit, update the `Company` and redirect to the `Company` objects' individual page (i.e. your READ route). Put a link to this route on the index page next to each company or on the company's individual page.

#### Delete

Finally, make a route that deletes a `Company` from the database. You don't really need a new page for this - just a route and a redirect. Put the link on the `Company` objects' individual page.

#### Bonus - the Admin

After you've created a few companies, follow this bit of the [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial02/) and connect to your built in admin backend. This is one of the best built-in features of Django that definitely makes your life a little easier (i.e. It does all your CRUD ;) ). Play around and take a look at its functionality.
