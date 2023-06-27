class animal :
    def speak(self):
        print('Animal Speaking')

class dog(animal):
    def bark(self):
        print('Dog barking')

d = dog() 
d.bark() 
d.speak()