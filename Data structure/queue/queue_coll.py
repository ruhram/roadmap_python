from collections import deque 

q = deque() 

# adding element to queue 
q.append('a')
q.append('b')
q.append('c')

print('Initial Queue : ')
print(q)

print('Print dequeue :')
print(q.popleft())
print(q.popleft())
print(q.popleft()) 

print('Print queue : ')
print(q)