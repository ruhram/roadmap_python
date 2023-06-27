class animal:
    def speak(self):
        print('Animal Speaking')

# The child class dog inherits the base class animal 
class dog(animal):
    def bark(self):
        print('Dog Barking')

# The child class Dogchild inherits another child class Dog 
class DogChild(dog):
    def eat(self):
        print('Eating bread ')

d = DogChild()
d.bark()
d.speak() 
d.eat()