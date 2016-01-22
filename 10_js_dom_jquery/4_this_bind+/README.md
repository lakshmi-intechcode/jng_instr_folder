# What is THIS?!?!?!

### Learning Objectives
***Students will be able to...***

* How to use This

---
### Context

* Using `this` is an essential JS function that will make cleaner more organized code

---
### Lesson

##### Part 1 - This Intro

* `This` is a javascript statement which will reference the value of a single object  at a specific moment in time
* Not only does it reference the object but it will have the value of the object
* In the global scope `this` will refer to the window object
	* open the inspector and type this
	* We don't usually use `this` in the global space, but more for functions
* The value of `this` will be the value of the object that invokes the function where `this` is located

***Five Min Exercise***

* Make a html file and a main js file. 
* Hook up the main.js file and [jQuery](https://cdnjs.com/libraries/jquery/2.2.0)
* Inside your html file make the boilerplate template and create a button in the body that says "CLICK ME"
* Inside your JS file use document.ready
* Now use jquery to target the button and on click console.log `$(this)`
* What do you get?
	
##### Part 2 - More of This!

* this does NOT have a value until something invokes the function where it is defined. 
* Do not get it mixed up. `this` does not reference the function/object where it is defined. It will get it's value from the object that invokes it. 

```
var myThis = function(x){
		console.log(this)
}

$("button").on("click", myThis)
```

##### Part 3 - Bind / Call / Apply

* Noticed what we did in the above example was a named callback
* What if we DID want to reference something inside of the callback function, and NOT the object value that invoked it
	* e.g. the myThis function instead of the button object
* That's where Bind / Call / Apply come in.
* You will need to `bind` the value to to the object value you want so `this` will not target the invoking object. 
* Check out the [JavaScript is Sexy Bind / Apply / Call Entry](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/)




