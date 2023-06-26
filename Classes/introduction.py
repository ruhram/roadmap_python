class dog :
    attr1 = 'mammal'
    attr2 = 'dog' 

    def fun(self):
        print("I'm a", self.attr1) 
        print("I'm a", self.attr2)

rodger = dog() 

print(rodger.attr1)
rodger.fun()