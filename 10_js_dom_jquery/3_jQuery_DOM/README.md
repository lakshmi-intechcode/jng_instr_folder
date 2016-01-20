# We are WRAPPING IT IN CA$H

### Learning Objectives
***Students will be able to...***

* Use the jQuery Library
* jQuery Selectors
* jQuery Methods
* jQuery DOM

---

### Context

* jQuery is used EVERYWHERE!!!

---

### Lesson

##### Part 1 - What is jQuery

* jQuery is a library
* We've been dealing with libraries since the first week of learning Python
* Libraries are just giant code bits that somebody else wrote to make our lives easier
* In the sense of JavaScript you may have to do several nested loops just to grab an element from the DOM. Something that can be solved with the `$` in jQuery
* jQuery is not only useful for helping to organize our own code but it is extremely popular with other JavaScript frameworks.
	* Bootstrap
	* D3.js
	* Foundation

##### Part 2 - jQuery download

* jQuery sounds pretty amazing. How do we link this to our file? 
* Well, the same way we can link our own JavaScript file. With the script tag

```
	<script type="text/javascript" src="main.js"></script>
```
* `IMPORTANT` your JS script will come AFTER any other 3rd party scripts such as jQuery
* Visit the jQuery website and download the latest version of jQuery.
* The location you put that in your computer you can now link it in the `src` attribute of the script tag
* Negatives
	* For organization you may have a jQuery file in each app folder
	* We'll have to gitignore the jQuery file every time we push to github
	* Also when we host our projects online we'll have to push our jQuery file to the server
* How can we fix this?!?!? 

##### Part 3 - Save Us CDNs!!!

* CDN stands for Content Delivery Network
* [jQuery CDN from cdnjs](https://cdnjs.com/libraries/jquery/)
* A CDN is a network where all these giant libraries/files are stored in some cloud somewhere. 
* We are able to access and use the libraries by linking to these CDNS

***Five Min Exercise***

* Make an index.html file
* Make a main.js file
* Link the main.js file to the index.html file
* Make boilerplate HTML template in your index.html file
* Enter the following code in your main.js file
* DO NOT copy and paste this, type the whole thing out

```
$(document).ready(function(){
	$("body").append("<h1>HELLO WORLD</h1>")
})
```
* Open the html file in your browser and check the console
* Link a jQuery file or CDN to the html
* Does it work now?

***NOTE***

* $(document).ready() is SIMILAR to window.onload in vanilla javascript
* The biggest difference is document.ready does not wait for as much content to load as the window.onload function.
* Check out this [Stack OverFlow Answer](http://stackoverflow.com/questions/3698200/window-onload-vs-document-ready) below.

```
The ready event occurs after the HTML document has been loaded, while the onload event occurs later, when all content (e.g. images) also has been loaded.

The onload event is a standard event in the DOM, while the ready event is specific to jQuery. The purpose of the ready event is that it should occur as early as possible after the document has loaded, so that code that adds functionality to the elements in the page doesn't have to wait for all content to load.
```

***NOTE NUMBER TWO***

* You may see some people do this:

```
$(function(){})
```
* We DO NOT use this syntax b/c it's a dumb shorthand and confusing. 
* It acts the same as `document.ready` so just use `document.ready`

##### Part 4 - Let's talk about $$$$$$

* How did we manipulate the DOM using vanilla JS yesterday?
	* document.getElementById()
	* document.getElementsByClassName()
	* document.createElement()
	* AND OTHERS
* The most often used jQuery statement is the `$`
* 


















