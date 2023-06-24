stack = []

#element in the stack 
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

#LIFO Order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)