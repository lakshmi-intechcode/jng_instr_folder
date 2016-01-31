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