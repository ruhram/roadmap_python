fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits] 
print(newlist)

newlist = ['hello' for x in fruits] 
print(newlist)

list = [x if x != 'banana' else 'orange' for x in fruits]
print(list)