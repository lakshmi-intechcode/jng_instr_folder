# MOAR JAVASCRIPT

### Learning Objectives
***Students will be able to...***

* Use ajax calls to talk to api's

---
### Context

* All people care about is speed, lets give it to them.

---
### Lesson

#### Part 1 - AJAX Intro

- AJAX stands for Asynchronous JavaScript And XML
- Remember when we dealt with API's the responses that came back to us were either in `JSON` or `XML`
- `XML` format used to be what was widely used and therefore it fit into the `AJAX` acronym.  
- You can ignore the XML part for now because as you know we are ONLY dealing with JSON formatted data
- We will be able to make requests using JavaScript
- Yay single paged applications!
- Examples of AJAX in use:
  - Think about how your email updates your inbox without you refreshing the page?
  - The constant newsfeed scrolling down on Facebook, Twitter, Tumbler, and the like

***WHY IS THIS SO GREAT?!?!?!***

* Our server will have to do less.
* We are putting more items on the client side
* There is a clearer line between what the front end will do and what the back end will do
* The Asynchronous ability of AJAX will allow faster response times

***WHAT PROBLEMS MIGHT WE FACE***

* The back button and the refresh button don't work with Single Page Apps
* JavaScript can be disabled by people (This is a crazy thing to do, i don't care about people who choose to turn off JS)

#### Part 2 - Practice

* Let's make an API request and get back some data using AJAX
* Make an HTML and a JS file

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

  <script src="main.js"></script>
</body>
</html>
```
* Run a console log in your js file to make sure it's connected

```
console.log("ELLO WARLD")
```
* Let's make a GET request to the OMDB api.
* Back to our go to movie. Grab the endpoint for top gun
* Now that its connected let's try this code in the JS file

```
console.log("ELLO WARLD")

  var request = new XMLHttpRequest();
  request.open('GET', 'http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json', true);

  request.onload = function() {
    // status codes below 200 and above 400 usually means there's an error
    if (request.status >= 200 && request.status < 400) {
      // If there was no error lets store the response and console log it
      var movie_response = request.responseText;
      console.log(movie_response);
    } else {
      // If we do get an error console log something to tell us
      console.log('SOMETHING IS WRONG!!!');
    }
  };

  request.onerror = function() {
    // Connection problem
    console.log('Dear client your connection sucks, get off comcast');
  };

  request.send();
```

***What the hell did we just do?***

* `request.open` - this takes three arguments.
  * `method` - first argument. What type of HTTP verb are we using?
  * `url` - second argument. What is the endpoint we are hitting
  * `async` - third argument. Is this call expected to be asynchronous
* When that request loads run the function
* Control flow statement to tell us if there is an error or not

#### Part 3 - jQuery AJAX

* What we just saw was how AJAX requests are made in Vanilla JavaScript

***Side Note***

* You should know how to do this or at least that it exists, there are many code challenges I know of that ask for things to be done in only Vanilla JS.

***Back to the lesson***

* WRAP IT IN CASH
* jQuery gives us several methods where we can shorten everything we did in the previous section into one command.

```
$(document).ready(function(){
  console.log("ELLO WARLD")

  $.ajax({
    method: "GET",
    url:"http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json",
    success: function(result){
      console.log(result);
    }
  })
})
```

#### Part 4 - HTTP CRUD

| HTTP Method | Action                        | Example URI                      |
|-------------|-------------------------------|----------------------------------|
| GET         | Grab data for ALL items       | http://movies.com/api/movies     |
| GET         | Grab data for a specific item | http://movies.com/api/movies/898 |
| POST        | Create a new item             | http://movies.com/api/movies     |
| PUT         | Update an existing item       | http://movies.com/api/movies/898 |
| DELETE      | Delete a specific item        | http://movies.com/api/movies/898 |

#### Part 5 - CORS: Cross-Origin Resource Sharing

* Since we are beginning to build web apps we'll need to get data from somewhere
* APIs are an essential part for building web applications, and making sure we can grab organized data to present to the user
* Since we will be targeting APIs that are not our own we may run into some of the following errors
	* `CORS`
	* `No Access Control Origin Allowed`
	* Other fun stuff
* These errors stem from the permissions during an interaction between two resources.
	1. Resource 1 - The browser on your computer making an ajax request to a Google API
	2. Resource 2 - The Google server that receives that request and decides to allow it and send a response

#### Part 6 - JSONP

* JSONP stands for "JSON with Padding"

***NEGATIVES***

* JSONP can only perform GET requests
* How sure are you that the server returns JSONP
	* If the server does not return JSONP you may get an error in your "AJAX Success Callback" that looks like:	* `Unexpected Syntax Token :` OR `Unexpected Syntax Token <`
* JSONP is not secure. 

***HOW THIS WORKS***

* JSONP allows us to send data because it utilizes the browsers parsing of a `<script>` tag and how script tags can have different sources from different origins
* We will use this to wrap our data inside of an object. 
* We will get a response back `(if the server allows JSONP)` in the form of JSONP
* If it does not support JSONP you may get errors such as `Unexpected Syntax Token :` OR `Unexpected Syntax Token <`
* This is because your browser may be expecting something back like this
	* `jQuery16406345664265099913_1319854793396({"red" : "#f00"})`
* Example Below:

```
$(document).ready(function(){
  console.log("ELLO WARLD")

  $('#button').on('click', function(event){
    event.preventDefault();

    var movie_searched = $('input[name="movie"]').val().replace(" ", "+")
    console.log(movie_searched);

    $.ajax({
      method: "GET",
      url: "http://www.omdbapi.com/?t="+movie_searched,
      dataType: "jsonp",
      success:function(response){
        console.log(response)
        $('.blah').append(response.Title)
      }
    })
  })
})
```
* This example uses an HTML form.
* We are grabbing the button and applying a click event to it
* The `event.preventDefault()` helps us to prevent the form from actually submitting and re-rendering the template
* The variable grabs the value and edits it so we can plug it into the url
* Make the ajax call as usual
* Add a `dataType: "jsonp"`


#### Postman

* This is an extension in chrome that allows you to make calls to an api to see what we can get. 
* It becomes handy when you want to test the other HTTP Methods on an API
* ***This is better than CURL***

#### Resources

* [http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about](http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about)
* [https://jvaneyck.wordpress.com/2014/01/07/cross-domain-requests-in-javascript/](https://jvaneyck.wordpress.com/2014/01/07/cross-domain-requests-in-javascript/)
* [https://www.html5rocks.com/en/tutorials/cors/](https://www.html5rocks.com/en/tutorials/cors/)
* [https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started)
* [https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)
* [http://code.tutsplus.com/tutorials/24-best-practices-for-ajax-implementations--net-9180](http://code.tutsplus.com/tutorials/24-best-practices-for-ajax-implementations--net-9180)