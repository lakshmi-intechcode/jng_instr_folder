# Python Fundamentals

### Learning Objectives

***Students Will Be Able To...***

* Create a variable in python
* Assign the different data structures to variables
* Write python statements using control flow
* Write python statements using loops and iteration

---
### Context 

* The fundamentals of programming translate throughout every language
* Like learning any new language we're going to start with the basics and build up
* If you wanted to learn english you wouldn't start by reading a novel, but with the alphabet

---
### Lesson

#### Part 1 - Variables

* Variables are a way to store and save data for use
* This is called `assignment`. You are assigning a value to a variable
* Declaring Variables
	* Do not need to use `var`
	* Cannot start with a number
	* Cannot declare with special characters
	* Written in snake case
* Open up Python in the terminal

```
name = "Jason"
fav_num = 8
turtles = ["Raph", "Leo", "Mickey", "Donny"]
```

#### Part 2 - Data Types

* Now you may have noticed that variables can hold different `types` of values
* These are called `Data Types`
	* Strings
		* Strings are immutable. Once they are declared they cannot be changed. You can add strings together to create a new string but you cannot mutate an already existing one
	* Numbers
		* Floats
			* decimals
		* Integers
			* whole number
	* Booleans
		* 0
		* ""
		* null
		* false

#### Part 3 - Math Operators and Boolean Operators

* Python comes with the following symbols for mathematical operators. 
* The language also supports PEMDAS
* `==`, `!=`, `<=`, `>=`, `<`, `>`
* Chaining Operators

```
1 < 2 < 3
//Is 1 less than two AND is two less than three
```
* Python also comes with these boolean operators
	* `and` == `&&`
	* `or` = `||`
	* `not` = `!`

***Five Min Exercise***


```
"A" == "A"
// True or False?

"5" == "5"
// True or False?

8.00 == 8
// True or False?

2 == "2"
// True or False?

Declare three variables and assign them three random numbers. 
Pass those variables to each other through chaining operators so that it will return True

Pass those variables to each other through chaining operators so that it will return False

For example: x < y < z == True || x < z < y == False
```

#### Part 4 - Control Flow

* Now we have reached `if/else` statements
* If an expression you passed in is `True` do something
* Else do something else

```
if expression == true:
	run code
	
if name == "Jason":
	print("That is an awesome name")
else: 
	print("You should get a different name")
	
if number > 100:
	print("That's a big number")
elif number > 50 && number < 100:
	print("That's a medium number")
else:
	print("Your number is puny")
```
* Things to note
	* You don't need parenthesis
	* Put a semi colon after the expression you want to evaluate
	* `if` to `elif` to `else`
	* Tab to show what part of the function belongs where

***Five Min Exercise***

* Declare two variables: hero and color
* Assign them whatever you want
* Write a if else statement that will...
	* print("Mashed Potatoes") if hero == color or False
	* print("Tacos") if hero is not the same as color
	* print("Oysters") otherwise

#### Part 5 - Lists and Indexing

* What if you wanted to store more data. 
* Can be assigned to variables
* Can hold different data types at once
* The values are indexed for us starting at zero

```
my_list = ["Jason", "Anna Kendrick", 2015, True]

my_list[0] == "Jason"

my_list[2] == 2015
```
* Just a heads up indexing through a list is similar to indexing with strings. 
* the value at index zero will be the first element in the list, or the first letter in a string

#### Part 6 - Functions and Statements

* We declare our functions with the word `def` for define
* Functions follow the same naming principles as declaring variables
	* Snake case
	* Do not start with numbers or special characters
* Remember how we used white space to organize our code with if/else statements. Well that idea holds true everywhere in Python

```
def my_name():
	print("My name is Jason")
```
* Functions allow us to build code that is reusable
* This follows the concept of `DRY - Don't Repeat Yourself`
* Functions can also take parameters. These allow our functions to be more dynamic

```
5 + 5 = 10

2 + 4 = 6

def add(x,y):
	print(x + y)
```
* Putting it all together
* Let's make a function that will take in a parameter

```

```
* Implicit returns = None
* 


#### Part 7 - Methods for Help

* `len()`
* `pop()`
* `append()`
* `split()`
