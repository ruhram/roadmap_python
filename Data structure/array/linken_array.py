class Node:
    def __init__(self) :
        self.value = 0
        self.next = None

head = None
one = None
two = None
three = None

#alocate 3 node in heap
one = Node()
two = Node()
three = Node()

#assign value values
one.value = 1 
two.value = 2 
three.value = 3 

#connect nodes 
one.next = two 
two.next = three 
three.next = None

head = one

while head != None :
    print(head.value)
    head = head.next
#print linked list 
