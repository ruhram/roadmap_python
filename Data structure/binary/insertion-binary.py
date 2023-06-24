#create node 
class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None 
        self.right = None 

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    
    return node 

def inorder(root): 
    if root is not None :
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

#Driver Code
if __name__ == '__main__':
    root = None 

    # inserting value 50
    root = insert(root, 50)

    # inserting value 30
    insert(root, 30)

    # inserting value 20 
    insert(root, 40) 

    # inserting value 60
    insert(root, 60)

    # Print BST 
    inorder(root)

    print(root.key)
