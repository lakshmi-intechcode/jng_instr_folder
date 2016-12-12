# Weekend Review

---

### HTML

* How is HTML5 different from HTML?
* What are semantic tags?
* What are the two default display properties for elements?
* What are some attributes we can apply to an HTML element?
* What kind of items go into the \<head\> of our document?
* What kind of items go into the \<body\> of our document?
* Why is HTML not considered a programming language?

### CSS

* What are the three ways to apply CSS to your HTML
* How do we target (or *select*) HTML elements using CSS?
* What is CSS Specificity? What is the order? 

### JavaScript

* How do for loops work in JS? While Loops?
* How do we write if else statements?
* What does string concatenation look like in JS?
* What are JS Arrays? JS Objects?

---

# What is the DOM

### Learning Objectives
***Students will be able to...***

* Navigate the DOM
* Target elements on the DOM
* Manipulate the DOM by...
	* adding
	* removing
	* changing
* Utilize JS Scope along with Higher Order Functions
* Start a GithubIO page. 

---
### Context

* Give the user more powerssss

---
### Lesson

##### Part 1 - Moar JavaScript Concepts

* JavaScript allows us to program in an Object Oriented Way or in a Functional way. 
* What is scope and how does it look in JavaScript? 
	* Scope is where data exists and is accessible from. 
	* Variables and Functions belong either to a local(also known as lexical) scope, enclosing scope, or a global scope.
* Variables declared in a function are in the local scope.
* Variables in the global scope are accessible anywhere.
* If you have nested functions variables in an outer function are accessible in an inner function. These are called closures.

##### Part 2 - Closures / Callbacks / Higher Order Functions 

* Let's take into account variables and functions as parameters. 
* All callbacks are closures but not all closures are callbacks.
* Callbacks are also known as "Higher Order Functions" but for the purpose of this course we will be sticking with the term "Callbacks".
* A callback is a function that has been created and defined but NOT invoked.
* Instead it is sitting around waiting to be "called back" by some sort of event such as a click event, or the invocation of another function. 
* See the calculator example from class below.

```
var add = function(a,b){
	return(a+b)
};

var sub = function(a,b){
	console.log(a-b)
};

var multi = function(a,b){
	console.log(a*b)
};

var calculator = function(a,b,callback){
	var myNum= 234
	var newVal = callback(a,b)
	
	return newVal
};

console.log(calculator(7,8,add))
```


##### Part 3 - What is the DOM?

* DOM = Document Object Model
* This is a convention for how HTML elements are represented in the browser.
* Every element is its own "node".
* You can visualize them as a tree.
* Utilizing JavaScript we are able to navigate and access this tree.

***Five Min Exercise***

* Google these functions/methods and write down what they do; we will come back as a class and talk about them:
* Targeting
  * `document.getElementById`
  * `document.getElementsByClassName`
  * `document.getElementsByTagName`
* Addition and Removal
  * `document.createElement`
  * `document.createTextNode`
  * `node.appendChild`
  * `node.removeChild`
  * `node.remove`
* Editing
  * `node.setAttribute`


##### Part 2 - Using DOM Methods

* Let's put what we researched to use.
* Pull up the whiskey code from yesterday.
* Link the main.js file.
	* Why did I put the script tag at the bottom of the html.
* Things to do:
	* Target specific element by id
	* Target elements by class 
	* Target elements by tag
	* Create a div
	* Give div content
	* Give the div an attribute
	* Put the div somewhere

##### Part 3 - DOM EVENTS!!!

* Everything revolves around events. 
* How can we make a click event in vanilla JS?
* JavaScript comes with an `addEventListener` method.
	* You may see the method called `onClick` but we will not be using that.
	* Try to stay with addEventListener.
* `addEventListener()` - is attached to a targeted element and takes in two arguments.
	* The first argument is an event passed in as a string.
	* Some events are:
		* click
		* mouseover
		* mouseout
	* The second argument is a block of code that will be run when the event is starts.	
	
```
var header = document.getElementById("myHeader")

var namedFunc= function(){
	alert("Does this work?")
}

header.addEventListener("click", namedFunc);

// header.addEventListener("click", function(){
// 	alert("Does this work?")
// })
```	

***NOTE***

* The first example is a `Named Callback`.
* the second example (commented out) is an `Anonymous Callback`.

##### Make a *FREE* Github.IO Home Page

* GitHub users are allowed to host a free home page at the URL `<your_username>.github.io`.
* This URL *serves* every file in a repository you create called `<your_username>.github.io`.
	* Go to `http://github.com/<your_username>`.
	* Create a new repository.
	* Call this repository `<your_username>.github.io`.
	* Clone it to your local development environment.
	* Create a file called `index.html`.
		* When a browser calls a location without specifying a resource, most servers default to responding with a page called `index.html`.
		* `index.html` is what will be displayed when someone points their browser at `<your_username>.github.io`.
* *Any* file you create will be viewable at the URL `<your_username>.github.io/<name_of_file>`.
	* This is also true of directories, i.e. `<your_username>.github.io/<name_of_directory>/<name_of_file>`.
	* A URL is *literally* a path to a `resource`, exactly mirroring your directory structure.
* Create another file, `cody-is-the-best.html`. Put some HTML in it.
	* How can you access this file with your browser?
* Within the `<your_username>.github.io` project, create a directory called `shenanigans`.
	* Within `shenanigans`, create another `index.html`.
	* What happens when you point your browser at `<your_username>.github.io/shenanigans/`?

Obviously, none of this works until you push the changes in your `<your_username>.github.io` repo to master. (Obviously.)
