import functools 

mylist = [11, 22, 33, 44] 

# Recursive Functional approach 
def sum_the_list(mylist):
    if len(mylist) == 1 :
        return mylist[0]
    else:
        return mylist[0] + sum_the_list(mylist[1:]) 

# lambda function is used 
print(functools.reduce(lambda x,y : x + y, mylist))