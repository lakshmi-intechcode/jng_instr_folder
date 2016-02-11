# I Mustache You A Question

#### Topics of Review

* AJAX
* Verbatim Tag
* Mustache Templating

#### AJAX

* AJAX stands for Asynchronous JavaScript and XML
* Instead of code reading top down, code is read Asynchronously
* Two or more functions can be invoked at the same time
* Multiple requests to your server or an API can be running at the same time
* The benefits to this is speed.
* The downside is the organization of code must be perfect
	* Request B cannot rely on the data of Request A if they are both Asynchronous.
	* What if Request A doesn't give the data back before Request B is run, then you'll get an error
* Check out the code below (from the included example)

```
		$.get({
			url: "search",
			data: {"title": movie_title},
			dataType: "json",
			success: function(data){
				console.log(data)
```
* `$.get` is making a `GET` request
	* You can also make a `POST` request using `$.post`
	* Best practice is to use `$.ajax` and inside a parameter is `type: "GET"` or `type: "POST"`
* The url is targeting a `urlpattern` inside of my `urls.py` file. 
	* It assumes it will be adding search to the domain you are already on, in this case it's `localhostL8000/movies`
	* You can also put in an endpoint of an API as well if you are not trying to get to a Django View
* `data` is passing a key:value pair to the `WSGI REQUEST` object that will hit Django. In this case the title will be located inside the `request.GET`
* `dataType` is used to help us with making request between browsers
* `success` is a callback function that will be invoked upon the "success" of the ajax request

#### DJANGO VIEWS

* Take a brief look at the example below (from the code) 

```
class Search_All(View):
	url = 'http://www.omdbapi.com/?s='
	# use requests params to dynamic url

	def get(self, request):
		title = request.GET["title"]

		search_title = title.replace(" ", "+")
		
		url_end = self.url + search_title

		# control flow status_code check
		omdb_req = requests.get(url_end).json()


		print(omdb_req)
		content = {
			"movie": url_end
		}
		return JsonResponse(omdb_req)
```
* This is the "view" the above ajax request is hitting
* I declared the endpoint of my omdb api
* Through regular python and django I 
	* concatenated some strings
	* imported the requests library to make the request to omdb
	* returned a `JsonResponse` that will go back to the ajax request
	* This response will hit the "success" part of the request

***note***

* There are some comments in there about using params through the requests
* I haven't gotten around to editing the example with it but feel free to research that on your own
* Also in the review session it was introduced that best practice is to test the status code
* Stick some control flow in there to ensure that you are getting back a successful request

#### VERBATIM

* The verbatim tag will wrap around your Mustache Template. 
	* This is IF you are creating your own file with a script tag to hold the information and load it
* Take the example below
* Base.html

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">

<head>
	<link rel="stylesheet" href="{% static 'css/style.css' %}">
	<meta charset="UTF-8">
	<title>GET REQUEST</title>
</head>
<body>

	<div class="container">
		{% block content %}

		{% endblock content %}
	</div>	

	<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.0/jquery.min.js'></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.min.js"></script>
	<script src='{% static 'js/main.js' %}'></script>

</body>
</html>
```
* index.html

```
{% extends 'base.html' %}

{% block content %}

	<h1> WE ARE IN INDEX </h1>
	
	<form action="" class='movie_form'>
		<input type="text" name='search_value' placeholder="Enter Movie Title">
		<input type="submit" name='search_button' value="Find Movie">
	</form>
	
	<div id="blah"></div>

	{%include 'movies/search_list.html' %}

{% endblock content %}
```
* list.html

```
{% verbatim %}
	<script id="list" type="x-tmpl-mustache">

	<h3>MOVIES</h3>
	
	<ul>
	{{#Search}}

	<img src="{{Poster}}">
		<li>
			Title: {{Title}}
		</li>
		<li>
			Year: {{Year}}
		</li>
		<li>
			Type: {{Type}}
		</li>

	{{/Search}}
	</ul>	

	<h4>{{Response}}</h4>

	</script>

{% endverbatim %}
```
* Code Flow
* The base template will load the static files and has a block to bring in external code
* The index file will load inside of that block
* Inside the index file there is a div with the id of `blah`
	* This is empty right now but will be used to place our Mustache items
* The index file also has an include tag that will load the information from the list.html
* The list.html file has a script tag (remember script tags are display none) that will load with the index
* It is surrounded by the `Verbatim` tag to PROTECT it from Djangos templating
* At this point you are telling Django "Hey these templates aren't for you" 
* Django will not try to populate the curly braces with data if they are surrounded by the script tag

#### Mustache Templating

* Our success callback will have something like this

```
			var template = $('#list').html();
			var renderM = Mustache.render(template,data);
			$('#blah').html(renderM)
```
* We are targeting a element with an id of list
* We use Mustache's "render" function to take the targeted template and load it with the data we got back earlier
* Use jQuery to target the div with the id of "blah" and change the inside of it's html with the variable of the rendered data
* Let's go back to the script template from earlier

```
{% verbatim %}
	<script id="list" type="x-tmpl-mustache">

	<h3>MOVIES</h3>
	
	<ul>
	{{#Search}}

	<img src="{{Poster}}">
		<li>
			Title: {{Title}}
		</li>
		<li>
			Year: {{Year}}
		</li>
		<li>
			Type: {{Type}}
		</li>

	{{/Search}}
	</ul>	

	<h4>{{Response}}</h4>

	</script>

{% endverbatim %}
```
* using `#` means to `enter` something. 
* In this example our data comes back with multiple `key:value` pairs
* One of those keys is `Search` that has an array of movies
* We use the `#` to target the `Search` keyword and then navigate the items inside of each element

***note***

* When Mustache is looking at the template it's strictly viewed as a `string`
* Take a look at the `Second Way` of doing the above. (Also found in the example code)

```
var tpl = "Movies:<ul>{{#Search}}<li>{{Title}} {{Type}}" + "{{Year}}</li>{{/Search}}</ul>";

var renderM = Mustache.render(tpl, data)

$('#blah').html(renderM)	
```
* With this we won't be needing that extra script/template file because we are creating the template inside our JS file





