def hello_decorator(func):
    def inner1(*args, **kwargs):
        print('Before Execution')

        returned_value = func(*args, **kwargs)

        print('After Execution')

        return returned_value 
    return inner1 

@hello_decorator 

def sum_two_numbers(a,b):
    print('Inside the function')
    return a + b 

a,b = 1,2 

print('sum = ', sum_two_numbers(a,b))