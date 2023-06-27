class bank:
    def getroi(self):
        return 10
class SBI(bank):
    def getroi(self):
        return 7

class ICIC(bank):
    def getroi(self):
        return 8 

b1 = bank() 
b2 = SBI() 
b3 = ICIC() 

print("Bank Rate of interest:",b1.getroi());  
print("SBI Rate of interest:",b2.getroi());  
print("ICICI Rate of interest:",b3.getroi());  