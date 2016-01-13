# JavaScript Introduction

### Learning Objectives
***Students will be able to...***

* Declare a variable in JavaScript
* Iterate through JS data structures
* Store JS data types in Objects 
* Use Control Flow in JS
* Use JS Process.Argv

---
### Context

* JavaScript is sexy. I'll show you why

---
### Lesson

##### Part 1 - A brief history. Why is this important?

* It's not, well not the history at least. JavaScript is used as the main front end language for web development, and is not growing in popularity as a backend language. 
* JavaScript was created in 10 days in 1995. 
* It was use to build the front end of websites, how they looked, and what users can do with them. 
* It was not until recently JavaScript could be used as a backend language
* This occured with the emergence of Node JS. A runtime environment that allows programmers to build server-side applications in JavaScript
* This has gained traction as it is convenient to build a full web application, the front and back, in the same language
* JavaScript has been around a very long time and has a lot of documentation on it. Google ALL YOUR QUESTIONS!

##### Part 2 - Node REPL

* We will be installing Node JS to use it's REPL environment in the terminal
* This is the same as the Python environment except it takes Node syntax

##### Part 3 - JS Syntax / Data Types / Data Structures

***Python***

* What do the following items look like in Python?
	* Variables
	* Assignment vs Comparison
	* Booleans
	* Numbers
	* Lists
	* Dictionaries
	* Strings

* JavaScript has many of the similar items but their syntax and the way we interact with them is very different

***Variables / Assignment / Comparison***

* Defining variables in JS
	*  `var` is placed in front of the variable name
	* DO NOT assign/create variables without using the word `var`, you will enter items into the global scope.
	* variables do not start with a number or special character
	* All things in JS are written in camelCase
* `Assignment is ONE EQUAL SIGN =`
* `Comparisons are THREE EQUAL SIGNS ===`
	* Two Equal signs as a comparator in JS exists but we NEVER USE IT!!!
	* It will check for value but not data type, it's essentially useless.
* We complete all our JS lines of code with semi colons
	
***Booleans***

* Same thing as Python. 
* Takes in the factors of True or False

***Numbers***

* Numbers are the same as well
* The only difference is in Python 2(which we aren't using) numbers with decimals are called Floats
* We don't have to worry about Floats in JavaScript and/or Python3

***Arrays***

* `Arrays` in JavaScript are like Lists in Python
* They are an iterable and their values can be targeted with indexes
* Written the same way with square brackets `[]`

***Objects***

* Now this can be a little confusing since in Python we referred to everything as an Object
* For the purposes of JavaScript we will be referring to Dictionary like structures as Objects
* You may also hear others call them associative arrays, but we will be calling them Objects
* Key:Value Mappings written the same way with curly braces `{}` and the key in quotes followed by a semi colon

***Strings***

* Strings are written the same way in JavaScript as in Python
* The only difference is the concatenation
* Concatenation can be done with plus signs `+` or commas `,`

```
var a = "Hello";
var b = "World";

console.log(a + " " + b)

console.log(a,b)

var x = "Beautiful "
var y = "People"

console.log(x.concat(y))
```
* There is no `.format` method or usage of `%` and `{}` as placeholders

##### Part 4 - JS Syntax Control Flow / Iteration

***Python***

* How are functions and methods written in Python?
* Control Flow
* Iteration / Looping

***Function Syntax***

* There are three ways to declare functions in JavaScript

```
function helloWorld(){
	console.log("Hello");
};

var helloWorld = function helloWorld(){
	console.log("Hello");
};

var helloWorld = function(){
	console.log("Hello");
};
```
* For this course we will be sticking with the last example of function declaration. This is because we want to be safe from `hoisting` bugs. You can google this on your free time if you'd like
* Remember all your JS syntax will end with a semi colon
* Function code blocks are put in between curly brackets `{}`
* White spacing does not have any relevance in JavaScript but we indent to make our code readable and organized

***Control Flow***

* JavaScript also offers us the use of the if/else statement. The syntax is much different

```
var deadpool = "Wade Wilson";

if (deadpool === "James Howlett"){
	console.log("Hey you're Wolverine");
} else if (deadpool === "Wade Wilson"){
	console.log("Here are your chimichangas");	
} else {
	console.log("You're not a super hero!")
};
```
* Differences
	* Wrap comparisons in parenthesis
	* End things with semi colons
	* Use curly brackets `{}` between each statement
	* Use three equal signs `===` for comparison

***Loops***

* The for loop is very different in JavaScript than Python

```
var animals = ["dog", "cat", "bird", "turtle", "fish", "hamster", "lizard"];

for (var i = 0; i < animals.length+1; i++){
    console.log(animals[i])
};

"dog"
"cat"
"bird"
"turtle"
"fish"
"hamster"
"lizard"
```
* Instead of a `for in` loop like Python we have the use of setting out own variable
* `var i = 0` is creating a variable called i that will start at zero
* `i < animals.length+1` - as long as this returns True the code in between the curly brackets will run 
* `i++` this will increment i after every loop iteration
* The for loop in JavaScript is much more dynamic because we can utilize i to grab different values for comparison.
	* e.g. 
		* increment by 2 to grab every other value
		* compare the value at the current index to a value at the previous index
		
* While loops are almost the same as Python but with all the usual JavaScript syntax

```
var i = 0;

while (i < 10){
    console.log(i)
    i += 1
};

console.log("all done!");

[output]
1
2
3
4
5
6
7
8
9
all done!
```

***Five Min Exercise***

* Write an application that will loop through the following JS Object and console.log the keys into one array and the values in separate array

```
var turtles = {
	"Raphael" : "Red",
	"Leonardo" : "Blue",
	"Donnatello": "Purple",
	"Micaelangelo":"Orange"
};
```

##### Part 5 - Process.ArgV

* This is the same idea as what we did with Python. 
* When we want to enter a value the usual syntax is 

```
var userInput = process.argv[2]
```
* Why is it two?
* Process.argv takes your command line arguments and returns them as an array
* The item at index zero will be "node" and the item at index one will be the file name











