# Advanced Python Techniques

### Learning Objectives
***Students Will be Able To***

* Use List Comprehensions with a imported csv file
* Use Python Generators to look through a iterable
* Use Kwargs inside of a Python method to print out unknown amount of arguments
* Declare specific methods to be "Class Methods"
* Python Collections

---
### Context

* We're going to get into some deeper Python understanding. This will help your code for the upcoming assignments

---
### Lesson

##### Part 1 - List Comprehensions

* Python comes with the ability to give us a list with one line of code
* List Comprehensions allow us to build a list of values by filtering through an iterable. 
	* We know that iterables are any data types / data structures that can be looped through. (strings, lists, tuples, and the like)
* The syntax for a list comprehension will look like this:

```
[ expression for item in list if conditional ]
```
* The expression is what you want to do to each item
* The for loop is... the for loop
* The conditional is an optional parameter. 
* Let's print out a list of all the numbers from 1 to 20

```
num_list = [num for num in range(20)]

// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

***Five Min Exercise***

* Write a method that will take in a string as an argument
* Use a list comprehension that will return a list with all the values being vowels
* Print out the number of vowels from the string that was inputed

##### Part 2 - Generators

* Generators allow us to blah blah

##### Part 3 - Kwargs

* Kwargs stand for Keyword Arguments. 
* They are some funky Python syntax. I have not seen kwargs used in another language other than Python. Nonetheless it can be useful in some use cases. 
* `**kwargs` allow us to pass in an unknown amount of arguments to a method using a KEYWORD

```
kwargs = {"first_name":"Volder", "last_name": "Mort"}

def hello(**kwargs):
	if len(kwargs) > 0:
		for key,value in kwargs.items():
			print("Your {x} is {y}".format(x = key, y = value))

hello(**kwargs)
```

***Five Min Exercise***

* Write a method that takes in kwargs with multiple key value pairs
* Return all the values that... BLAH BLAH BLAH FIGURE SOMETHING OUT

##### Resources

* [Python Tips Args and Kwargs](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)