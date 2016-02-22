# Calling All Autobots!
---

#####  Objective 1
* Write a function that accepts a string as an argument. 
* Transform every word in that string to title case
	* The first letter of every word should be capitalized
	
##### Objective 2
* The same function should take in a second argument.
* This argument will be a list of words called `exceptions` 
* The words in the list will not be title cased/capitalized if they are located in the string that was passed in. 

```
exceptions = ['the', 'and', 'decepticons', 'to']

titlecase(string, exceptions)
// Optimus Prime and the Autobots Assembled to Fight the decepticons
```


##### Object 3
* Write a function that will take a string and a list of words as arguments. 
* If the words in the list are located in the string, turn all their letters uppercase. 
* Otherwise leave the words not in the list alone. 

```
exceptions = ['optimus', 'prime', 'autobots', 'victorious']

titlecase(string, exceptions)
// OPTIMUS PRIME and the AUTOBOTS were VICTORIOUS in the battle of the bulge
```

##### Resources

* [title case](http://en.wikipedia.org/wiki/Letter_case#Headings_and_publication_titles)
* [LC Hawk](http://www.secnetix.de/olli/Python/list_comprehensions.hawk)
* [LC Read The Docs](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Comprehensions.html)
* [Python For Beginners](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
* [Dive Into Python 3](http://www.diveintopython3.net/comprehensions.html)