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

---
### Context

* Give the user more powerssss

---
### Lesson

##### Part 1 - JavaScript Scope

* What is scope and how does it look in JavaScript? 
* Scope is where the variable exists and is accessible from. 
* Variables either belong to a local scope or a global scope
* JavaScript follows function level programming, which we will touch upon more later
* Variables declared in a function are in the local scope
* Variables in the global scope are accessible anywhere
* If you have nested functions variables in an outer function are accessible in an inner function. These are called closures

##### Part 2 - Closures / Callbacks / Higher Order Functions 

* Lets take into account variables and functions as parameters. 
* All callbacks are closures but not all closures are callbacks
* Callbacks are also known as "Higher Order Functions" but for the purpose of this course we will be sticking with the term "Callbacks"
* A callback is a function that has been created and defined but NOT invoked.
* Instead it is sitting around waiting to be "called back" by some sort of event such as a click event, or the invocation of another function. 
* See the calculator example from class below

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


##### Part 1 - What is the DOM?

* DOM = Document Object Model
* This is a convention for how HTML elements are represented in the browser
* Every element is it's own "node"
* You can visualize them as a tree
* Utilizing JavaScript we are able to navigate and access this tree

***Five Min Exercise***

* Google these functions/methods and write down what they do
* We will come back as a class and talk about them
* Targeting
  * `document.getElementById`
  * `document.getElementsByClassName`
  * `document.getElementsByTagName`
* Addition and removal
  * `document.createElement`
  * `document.createTextNode`
  * `node.appendChild`
  * `node.removeChild`
  * `node.remove`
* Editing
  * `node.setAttribute`


##### Part 2 - Using DOM methods

* Let's put what we researched to use
* Pull up the whiskey code from yesterday
* Link the main.js file
	* Why did I put the script tag at the bottom of the html
* Things to do
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
* JavaScript comes with an `addEventListener` method
	* You may see the method called `onClick` but we will not be using that
	* Try to stay with addEventListener
* `addEventListener()` - is attached to a targeted element and takes in two arguments
	* First argument is an event passed in as a string
	* Some events are:
		* click
		* mouseover
		* mouseout
	* The second argument is a block of code that will be run when the event is starts	
	
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

* the first example that is an example of a `Named Callback`
* the second example that is commented out shows us an `Anonymous Callback`

	
	
	
	
	
	
	
	
	
	
	
	
	
	

