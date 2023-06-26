# Class for dog 
class Dog :

    # Class Variable 
    animal = 'dog'

    # The init method or constructor 
    def __init__(self, breed):
        
        # Instance Variable 
        self.breed = breed 
    
    def setColor(self, color):
        self.color = color 
    
    def getColor(self):
        return self.color

Rodger = Dog('pug') 
Rodger.setColor('brown') 
print(Rodger.getColor())