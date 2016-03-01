### RPG Refactor

* We learned a lot about SQL CRUD today but for tonights exercise we will be staying away from SQL
* Instead I want you guys to get some practice on building something in an MVC format
* We will be specifically focused on the Views and Controllers in this assignment and not so much the Models (since they talk to the DB)

#### Objectives

* Refactor your RPG game from the weekend
* You will be making a new python file for views
* You will be making a new python file for controllers
* Remember you will need to import the `class View` from the view.py while
* Make sure all your print statements that are intended for the User will be in the `Views`
* Your controller will hold the game logic

***Importing Example***

```
from view import (className)

class controllerClassName:
	
	def __init__(self):
		self.view = className()
```
* After you are done think about how you will build out your game further
* Write out User Stories and Pseudo Code how you will save user data. 
	* What will the table look like? 
	* What will the columns be? 
	* What will the queries look like for the interaction? 
	* Can a user login? Will they have a username and password?