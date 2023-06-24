from queue import Queue 

q = Queue() 

print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print('Full : ', q.full())

print('Element dequeued : ')
print(q.get())
print(q.get()) 
print(q.get()) 

print('Empty : ', q.empty())
print('Full : ', q.full())

