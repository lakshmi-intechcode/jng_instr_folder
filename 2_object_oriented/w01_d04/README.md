# Object Oriented Programming Day 2

### Learning Objectives
***Students Will Be Able To...***

* Utilize classes using Inheritance
* Use items from a parent class
* Use items from a child class
* Utilize the terminal to help research

---
### Context

* This is the last topic of object oriented programming.
* Inheritance allows us to organize our code every more regarding objects

---
### Lesson

#### Part 1 - OOP 5 min recap

* Yesterday we were introduced to the idea that everything in Python is an Object
* We wrote classes
* Instance Variables vs Instance methods
* Scope - LEGB

#### Part 2 - Inheritance

* Make a class Pet
* Make a class Dog
* Make a class Cat
* Make a class Bird

```
class Pet:
    eyes = 2
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You got a new pet")

    def jump(self):
        print("your pet is jumping")

class Dog(Pet):
	
	def __init__(self,name, age, fluffy):
        Pet.__init__(self, name, age)
		self.fluffy = fluffy
		
    def speak(self):
        print("Bark Bark")

class Cat(Pet):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")
        
shadow = Dog(name = "Shadow", age = 17, fluffy = "yes")

lucy = Cat(name = "Lucy", age = 13)

shadow.eyes
lucy.legs
shadow.speak()
lucy.speak()

```
* The local method takes precedent over the parent method
* Brought up in class: If all pets have a name and an age we can put it in the parents `init` method
	* To utilize the parent `init` method we could call it inside of the child's `init` method and pass the values through to the parent

***Five Min Exercise***

* Make a parent class called `Vehicle`
* Make three child classes: `Car`, `Truck`, `Motorcycle`
* Instantiate the child classes
* Each child should have their own unique methods that will return an instance variable
* Each child should also have access to variables inside of the parent class

#### Part 3 - Terminal

* help()
* dir()
* "_"

#### Misc

* `input()`
* pseudo code
* user stories

