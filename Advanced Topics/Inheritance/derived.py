class calculation1:
    def summation(self, a,b):
        return a+b 

class calculation2:
    def multiplication(self, a, b):
        return a * b 

class derived(calculation1, calculation2):
    def divide(self, a,b):
        return a / b 

d = derived() 
a = 10 
b = 20
print(d.summation(a,b))
print(d.multiplication(a,b))
print(d.divide(a,b))