# Python Fundamentals Day 2

### Learning Objectives

***Students Will Be Able To...***

* Use Git to pull down repos
* Use the Command Line to Navigate the terminal
* Assign a dictionary to a variable
* Navigate a dictionary
* Use the datetime library
* Use the File I/O library
* Use Recursion

---
### Context

* Git is used universally by programmers to collaborate with each other
* Command Line is the way to talk to your computer
* More data structures
* Modules and Libraries provide useful add ons should we want to use something that makes our lives easier

---
### Yesterday in Depth

* What built in functions did you use?
* mutable vs immutable data structures 

### Lesson

#### Part 1 - Git
**10 min**

* Git is a collaboration tool that is universally used by programmers
* Below are the commands in git we will be using the most:
* `git init` - initialize a connection between that folder and git
* `git add` - show off your updates / differences between the repos
* `git commit -m "message here"` - add a message to this instance
* `git pull origin branch_name` - pull down the updates/changes from a repository
* `git push origin branch_name` - push up your changes to a repository
* `git checkout -b branch_name` - change to a different branch on your local machine, or create a new branch on your local machine
* `git status` - tells you what changes are in this folder and what branch you are on

***Notes***

* All of your daily repos will be done with branches

#### Part 2 - Command Line
**5 min**

***NEVER DO RM -RF AND PRESS ENTER***

* Check out this tutorial. It is extremely valuable to know how to navigate your computer using the CLI
* [http://cli.learncodethehardway.org/book/](http://cli.learncodethehardway.org/book/)
* Some common commands we'll be using are 
* `ls` - list the files in the folder
* `mkdir` - make directory, make a folder
* `touch` - make a file
* `pwd` - print working directory, this will give you the path in your computer where you currently are
* `cd` - change directory
	* `cd` by itself will bring you to your root folder
	* `cd ..` will bring you up one folder
	* `cd folder_name` will take you to that folder

#### Part 3 - Dictionaries 
**10 min**

* Dictionaries are similar to hashes in Ruby or associate arrays in JS
* They are Key Value data structures
* Instead of indexing through them to grab values, we can simply call the key

```
tmnt_colors = {
	"Leo": "red",
	"Raph": "blue",
	"Mickey": "orange",
	"Donny": "purple",
}

tmnt_colors[Raph]
```

***Five Min Exercise***

* Create a dictionary
* Using a for loop how can we print all the keys from the dictionary
* Using a for loop how can we print all the values from the dictionary

***Instance Methods***

* .get - "acts as is key in this dictionary"
* .values - gives a list of values
* .keys - gives a list of keys
* .items - gives the keys and values as tuples in a list

---
### BREAK
---

#### Part 4 - Built in Functions / Built in Methods / Modules

* Hopefully throughout your exercises yesterday you were able to find out about Python's built in functions. 
* Some of these may have proven useful to you
	* `len()`
	* `range()`
	* `split()`
	* `pop()`
	* `append()`
* These built in functions are bits of code that somebody wrote for us to use. They are out of the box and are ready to be used the moment you make a python file
* Modules are files that do not come out of the box with python3
* We can import these modules for use

#### Part 5 - Datetime

* Datetime is a module that comes with Python 3
* Show them importing

```
import datetime

from datetime import datetime
```
* The first option will import the whole module
* The section option allows us to import the class that we want
* One thing to note is that, if you import the whole module at once, you will have to invoke the class you are trying to call

***Five Min Exercise***

* Go through the `datetime` documentation. Make sure you are looking at Python3 docs
* What are some useful methods we can use with `date` and `datetime`
* What do they do?

***Examples***

* time is a class = hour, minute, second, ms
* date is a class = mm dd yyyy
* datetime is a class = year month day hour minute second ms
* You can only subtract a date instance from a date instance and a datetime from a datetime

```
import datetime

clock = datetime.time(10, 20, 56)

print clock.hour 
print clock.minute



this_day = datetime.date.today()

print this_day.year
print this_day.day
```

***NOTE***

* There are two other libraries that are similar. They are `calendar` and `time`. Most problems can be solved using the `datetime` library so for the purposes of this course we will try to stay using only this library

#### Part 6 - File I/O

* You do not need to import a library
* Make sure you use the `with` statement to open the file. 
```
with open(targetfile) as variable:
```
Here's how I *usually* read a text file with Python:
```
with open('filename.txt') as fp:
    for line in fp:
        print line
```

***Five Min Exercise***
What are these? How are they similar and different?
* `.read()`
* `.readline()`
* `.readlines()`
[You can read more here in a beginners tutorial](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python).
Or [here in the Python Docs](https://docs.python.org/2/tutorial/inputoutput.html).

#### Part 7 - Recursion

* When a function calls itself inside of itself.
* CS50 has a good video about this concept. [You should watch it](https://youtu.be/oWDKy0sKFyQ?t=6m20s).
There's also a good [explanation of the concept here](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion).

#### Misc. Some built in functions that can help

* `zip()`
* `recursive functions`
* `with file_name as name_for_code:`

#### Resources
* [http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
* [https://docs.python.org/2/tutorial/inputoutput.html](https://docs.python.org/2/tutorial/inputoutput.html)
* [CS50 Recursion Video](https://youtu.be/oWDKy0sKFyQ?t=6m20s)
* [https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion)
