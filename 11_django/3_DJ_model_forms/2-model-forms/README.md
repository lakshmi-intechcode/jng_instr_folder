User Login App
=================

Out of the frying pan and into the fire! Are you ready? You're going to be setting up your own Django project from scratch.

#### Set Up

First things first, set up your virtual environment in this folder.
```
virtualenv venv
source venv/bin/activate
pip3 install django-toolbelt
```
Now start a new Django project.
```
django-admin.py startproject <your project name>
cd <your project name>
python3 manage.py startapp users
```
Now we have our virtual environment & Django project set up, we'll still need to make some adjustments.

### Update settings.py 
Go into `settings.py` and do the following:
- Add your `users` app to the installed apps list
- Change your database settings to your local Postgres server.
```py
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'users',
		'USER': '<username>',
		'PASSWORD': '<password>',
		'HOST': '127.0.0.1',
		'PORT': '5432',
		}
	}
```
Now that our Django project can recognize the `users` as well as use Postgres for a database, we will still need to create our `users` database.

Opne up a terminal and run:
```
createdb users
```
### Update project/urls.py 
Go into `urls.py`in your project folder:
- Declare a `/users` app-level wide route that will route users app `urls.py`.
     * Hint: You will need to create the `urls.py` file within your Users app. Copy paste the contents from the generated `project/urls.py` for reference.   

### Update users/urls.py
- Since we copy-pasted from the project-urls, we will need to delete the `/users` route 
- Make a home `/` route in your new `users/urls.py` to go to `users.views.index`

### Update users/views.py
We should now have our URLs pointing in the correct direction. Let's run our server and head to `localhost:8000`. We shoud expect Django to return an error regarding either our index function not being defined, so let's create it!
- Create your index function in `users/views.py`. Tell it to render the users/index.html template.

What? That doesn't exist either?!? Inside your users folder, create a new directory called `templates`. Inside that, create an `index.html` file. (Don't forget to add something to the page so we can ensure it renders on load.)


### Create users/forms.py
Finally, we're going to need one more file to contain our ModelForms. Create a file in your users directory called `forms.py`. At the top, add the following:
```py
from django import forms 
```
Let's run your server, make sure it's working, fix any errors, and make a commit here in case it all breaks! Once you've done all that, We're finally set to begin!

#### Models and ModelForms

- Create a `User` model. The User table should look like this:
    ```
    username
    password
    created_at
    updated_at
    ```
- See the optional arguments for the DateTimeField for created_at and updated at [here](https://docs.djangoproject.com/en/dev/ref/models/fields/#datetimefield)
- Migrate the table to your database.

Now let's create a [ModelForm](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelform). A ModelForm is a form that Django will create for you based on a model using the given and/or specified fields. In `forms.py`, import your User model.

Now create the form class.
    ```py
    class UserForm(ModelForm):
    		class Meta:
    				model = User
    				fields = ['username', 'password']
    ```

#### Views and Templates

In `views.py` import the `UserForm` class. Now in your index route, create an instance of `UserForm` and pass it to your template.
```py
return render(request, "users/index.html", {'form':UserForm()})
```
In your `index.html` template, render the form.
```html
<form name="user" action='/create' method="POST">
	{% csrf_token %}
	{{ form.as_table }} <!-- can also be form.as_p, form.as_ul -->
<input type="submit" value="Create User">
```
Reload your server and you should see your form there.

#### The POST Route

Of course, that form is useless without a place for it to go. Create your `/create` route and view function. You can now create a User by submitting this form in your `views.py`
```py
new_user = UserForm(request.POST)
new_user.save()
```
Create a new page to redirect to after saving to the database that says "Welcome Username!" and shows when they were created. That route should be something like:
```
http://localhost:8000/u/<username>
```
Commit and Push this. We're going to be using this same project for the next exercise, so don't go too far.
