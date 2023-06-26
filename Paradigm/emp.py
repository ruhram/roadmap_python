# class emp has been defined here 
class Emp:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def info(self):
        print('Hello, % s. You are % s old.' %(self.name, self.age))
    
# Objects of class emp has been 

emps = [Emp('John', 43),
        Emp('Hilbert', 16),
        Emp('Alice', 30)]

# Objects of class Emp has been used here 

for emp in emps :
    emp.info()