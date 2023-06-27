tup = ('a', 'b', 'c', 'd', 'e') 

tup_iter = iter(tup)

print("Inside Loop : ") 
for index, item in enumerate(tup_iter):
    print(item) 
    if index == 2:
        break 

print("Outside Loop : ")
print(next(tup_iter))
print(next(tup_iter))
