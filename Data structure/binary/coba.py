class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None

def insert(node,key):
    if node is None:
        return Node(key)
    
    if key < node.key :
        node.left = insert(node.left, key)
    elif key > node.key :
        node.right = insert(node.right, key) 

    return node

def inorder(root): 
    if root is not None :
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None

root = insert(root, 5)

insert(root, 3)

insert(root, 6)

insert(root, 10)

inorder(root)

#print(root.right.key)