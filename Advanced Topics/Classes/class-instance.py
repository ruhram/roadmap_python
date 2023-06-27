#class for dog 
class dog :
    
    # class variable 
    animal = 'dog' 

    # The init method or constructor 
    def __init__(self, breed, color):
        
        # Instance Variable 
        self.breed = breed 
        self.color = color 

# Object of dog class
Rodger = dog('Pug', 'brown') 
Buzo = dog('Bulldog','black') 

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
print("\nAccessing class variable using class name")
print(dog.animal)