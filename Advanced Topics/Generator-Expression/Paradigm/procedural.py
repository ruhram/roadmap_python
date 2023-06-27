# Procedural way of finding sum of a list 

mylist = [10,20,30,40]

# modularization is done by 
def sum_the_list(mylist):
    res = 0
    for val in mylist:
        res += val 
    return res 

print(sum_the_list(mylist))