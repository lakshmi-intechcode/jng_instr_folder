# Todos API with AJAX

##### Description

* Time to make use of that awesome Todos API you wrote yesterday
* Lets combine that with our lesson today and build a Single Page CRUD application
* This application will never reload or redirect. (Your back button and refresh button will not work the same as server side rendered applications)

##### Objectives

* You will be making a BRAND NEW DJANGO PROJECT
* This project will be a Single Page application that will CRUD to the Django API you just built
* Make sure to include:
	* jQuery CDN - for easy ajax calls
	* [Mustache.js](https://github.com/janl/mustache.js) - This is a templating library that you can use to enter dynamic data to your template. Very similar to how we render information when building our other CRUD django projects
	* jQuery Cookies 
		* `<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>`
* You can have two applications running at the same time but change the port of one of them to `8080`

##### User Flow

* When the user hits the site, jQuery Cookie should look for a user cookie containing the API key. If it's not there, show them the sign up / sign in form in a modal. When they sign up, set the cookie with the API key.
* If the cookie is there, it should load their todo list using AJAX.
* The HTML page should update appropriately
* Add CRUD functionality
	* View the whole list
	* View specific ToDo
	* Edit
	* Delete
	* Add
* Have all the information render dynamically on the page using Mustache.js
* Here is an example of how your `list view` might look in HTML:

```
	<h1>Todos: </h1>s
	<ul class='todos'></ul>
```
* And how it'll look in JS

```
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

##### WORK FLOW

* This is a group weekend project
* PSEUDO CODE / USER STORIES / WIRE FRAME
	* How many buttons should there be?
	* How will the todos look?
	* Where will they go on the page?
* Use Trello to organize your project needs
	* Invite me to the project board
* Make one repository to work off of
	* Invite me to the repo
	* Utilize Git issues
	* Vote on who is the Git Czar
 
##### Tips

* Don't forget about event delegation. You'll probably need it.
* Use Mustache liberally, and definitely for your forms!
* Plan your DOM carefully, and do at least _some_ CSS styling.
