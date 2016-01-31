# MOAR DJANGO FEATURES

### Learning Objectives
***Students will be able to...***

* Use Class Based Views over Function Based Views
* Use `sessions` to store data

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Static Files

* Static File notes have been in your parking lot but we'll go over them briefly
* `Static Files` are your
	* images
	* CSS stylesheets
	* JavaScript files
* Here are the Django docs for how to set them up [static folder documentation](https://docs.djangoproject.com/en/1.8/howto/static-files/)
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


##### Part 2 - Class Based Views



##### Part 3 - Two Apps

* Very brief discussion
* Using multiple apps is just a matter of importing them
* We've done this already by importing models from `forms.py`
* Now we'll just be targeting an outside application
* The below example will be in your `project/posts/views.py`

```
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from Users.models import User

def user_post(request):
	user = User.objects.get(email=email)
```


##### Part 4 - User Sessions