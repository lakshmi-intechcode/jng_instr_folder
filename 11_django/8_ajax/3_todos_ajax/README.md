# Todos API with AJAX

##### Description

* Time to make use of that awesome Todos API you wrote yesterday
* Lets combine that with our lesson today and build a Single Page CRUD application
* This application will never reload or redirect. (Your back button and refresh button will not work the same as server side rendered applications)

##### Objectives

* This will be using strictly an HTML, CSS, and JS file
* Inside your HTML include the following
	* jQuery
	
* make ajax request
* if token comes back stores as a cookie
* use cookie to authenticate future request

bonus, updating features?


refactor the request, jquery 

if request is ajax 



#### Structure

We're going to load all the HTML once, the first time the user hits the page. So add an index route to your API project that renders an HTML file. The HTML file should have our site's general structure - all the HTML elements that create the template for your page, such as divs, a tags, p tags etc.

Inside that HTML file, we're going to need some JavaScript libraries.
```html
<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/mustache.js/0.8.1/mustache.min.js"></script>
```

That's jQuery, jQuery Cookie, and Mustache.

jQuery Cookie lets us load and store cookies from the front-end, like so:
```js
$.cookie('key') // get
$.cookie('key', 'value') // set
```
[Mustache](https://github.com/janl/mustache.js) is a front-end templating engine, much like Django's engine. This way we don't have to write lots of HTML.

You're also going to need to link your own JS file and CSS file from static files.

#### Flow

When the user hits the site, jQuery Cookie should look for a user cookie containing the API key. If it's not there, show them the sign up / sign in form in a modal. When they sign up, set the cookie with the API key.

I think this is a good place for a modal because we still want all of our DOM structure present - we just want to give the user a pop up to login from that we can show and hide with jQuery. If you have another idea that's fine.

If the cookie is there, it should load their todo list using AJAX.

At the bare minimum, there should be elements on the page that trigger AJAX calls to your API to load their todos, add a todo, update a todo, and delete a todo. How you want to design this is up to you.

Of course, the page's HTML should update appropriately. That's where Mustache comes in.

#### Mustache

Also in our index.html, we're going to want to define some Mustache templates. Again, these are very similar to Django templates.

Try this basic one for your `get_all_todos` endpoint. This goes in the `<body>` of the html document. This assumes that the endpoint returns a list of JSON objects with keys: `description` and `completed`
```html
<h1>Todos: </h1>s
<ul class='todos'></ul>
```
For your JS file, here's the corresponding AJAX request and jQuery to put it on the page:
```js
 $(document).ready(function(){

 	var todoTemplate = "<li>Task: {{description}}, Completed?: {{completed}}</li>"

 	function addTodo(todo) {
 		$('.todos').append(Mustache.render(todoTemplate, todo));
 	}

	$.get('/all', function(todos){
		$.each(todos, function(i, todo){
			addTodo(todo);
		});
	});

});
```
#### Tips

Don't forget about event delegation. You'll probably need it.

Use Mustache liberally, and definitely for your forms!

Plan your DOM carefully, and do at least _some_ CSS styling.

If you don't have good error handling in your API, you'll need it now. Think about user experience.
