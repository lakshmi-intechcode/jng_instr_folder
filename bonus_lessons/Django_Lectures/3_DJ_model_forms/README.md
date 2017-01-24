# Django Model Forms

### Learning Objectives
***Students will be able to...***

* Use Django Model Forms

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Model Forms

* So we've been building out HTML forms from scratch.
* It was great to learn about GET, POST, and Action
* Today we will be learning about Model Forms
* Django allows us to render HTML forms using Model fields

***The six bullets of Model Forms***

* [Taken from pydanny](http://www.pydanny.com/core-concepts-django-modelforms.html)
	* Model forms render Model fields as HTML
	* Model forms select validators based off Model field definitions
	* Model forms don't have the display/change all available fields
	* Model forms save dictionaries to SQL tables
	* forms are just python constructs
	* forms validate python dictionaries


##### Part 2 - My Whiskey Blog Steps

* Make your virtual env
* start project
* start app
* connect your app
* make models

```
from django.db import models

class Post(models.Model):
	brand = models.CharField(max_length = 50)
	brand_type = models.CharField(max_length = 80)
	description = models.TextField()
	price = models.DecimalField(max_digits = 6, decimal_places = 2)

	def __str__(self):
		return self.brand
		# return "{} {}".format(self.brand, self.brand_type)
```
* make forms file
* make forms models

```
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"brand",
			"brand_type",
			"description",
			"price",
		]
``` 
* make urls

```
from django.conf.urls import url
from django.contrib import admin

from .views import(
	posts_list,
	posts_detail,
	)

urlpatterns = [
	url(r'^$', posts_list, name='list'),
	url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
]
```
* make views

```
from django.shortcuts import render, get_object_or_404
from django import forms
from .models import Post
from posts.forms import PostForm

def posts_detail(req, id=None):

	whiskey = get_object_or_404(Post, id=id)
	mf = PostForm()
	print(mf)
	context = {
		"whiskey": mf,
	}
	return render(req, "posts/detail_view.html", context)
```

* make templates

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

	<form method="POST" action="">

	{{ whiskey }}		

	</form>

</body>
</html>
```

