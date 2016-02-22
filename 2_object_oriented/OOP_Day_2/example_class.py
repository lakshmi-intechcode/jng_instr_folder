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