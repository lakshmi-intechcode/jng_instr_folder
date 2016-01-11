# Advanced Python and Some Population Stuff

##### Description

* Okay so I couldn't find a easily downloadable file for fun data like movies or music, so we're going to use this bland population data
* There are multiple prompts in this README. The second half of the homework will be using the population.csv file
* Once you are finished with these prompts refactor your weekend terminal trader application, and complete the vocabulary review if you have not done so. 
 
***NOTE***

* Don't forget you have access to Pythons built in methods. (`sort`, `reverse`, and the like)


##### Objective 1 - Evens

* Take an integer as an argument
* Return a list where all values are the even numbers up until the argument
* Use a ternary operatory

##### Objective 2 - Vowels

* Take a string as an argument
* Use list comprehension to see if the string is a palindrome
* Palindrome is a word or phrase that is the same forward as it is backwards

##### Objective 3 - Reverse

* Take a string as an argument
* Return a list where all the values are the characters of the string in reverse

##### Objective 4 - Fibonacci

* Lets do fibonacci using Generators
* If you need a refresher the Fibonacci sequence is a sequence that starts with 0, and 1, and every following number is the sum of the previous two.

```
0,1,1,2,3,5,8,13,21
```
* Lets write a method that takes in a number as an argument and prints out all the numbers in the fibonacci sequece up to the input, USING GENERATORS

##### Objective 5 - FizzBuzz

* Lets do fizzbuzz using Generators
* If you need a refresher FizzBuzz is a programming exercise where if a number is:
	* Divisible by 3 print Fizz
	* Divisible by 5 print Buzz
	* Divisible by both 3 and 5 print FizzBuzz
	* Not divisible by 3 or 5 print the number itself

```
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz
```
* Write a method that will take in a number as an argument and print out all the numbers/fizzbuzz/ in that sequence, USING GENERATORS

##### Objective 6 - Random

* use the random library
* print out a random number from two given inputs
* Use A Generator

```
import random

def rand_num(a,b):
	pass
	
rand_num(34, 98)
```

##### Objective 6.5 - BONUS 

* Use the timeit module
* Write a function that will take in a number and print out all numbers from zero to input (Use Lists)
* Now do the same thing but with a Generator
* Time both functions and log the speed difference

### Using Population.csv

##### Objective 7 - States

* How many people live in 'CA'
* How many people live in 'FL'
* How many people live in 'NJ'

##### Objective 8 - Age

* Take in two numbers between 1 and 100. How many people have an age between those given numbers
  
##### Objective 9 - Ethnicities

* Print out the ethnicities and the number of individuals for each ethnicity

##### Objective 10 - Population Ranking

* Print out the top 10 most populated states and their population, in order from largest to smallest

##### Objective 11 - Age Compare

* Write a method where a user can input one state or several states
* Return the average age of all the people in those state, in order from highest to lowest

