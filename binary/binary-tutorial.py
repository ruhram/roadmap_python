class binary_tree:
    def __init__(self, key)   #function to insert data to our binary tree
        self.leftchild = None #setting leftchild of the tree to add items
        self.rightchild = None #setting rightchild of the tree to add items
        self.key = key
    class binary_tree:
        def __init__(self): #generate a tree to hold values 
            self.root = None
        #this is the end 
        def add(self, value): #function to add data items to the tree
            if self.key is None:
            self.key = data #begin adding elements to the binary tree
            return
        if self.key == value:   # this will take care for duplicate nodes
            return              
        if value < self.key:  #if value of the key node is more than the leftchild accept values
            if self.leftchild:
                self.leftchild.add(value) #set values to the leftchild of the tree
            else:   
                self.leftchild = binary_tree(value)
        else:   #values are more than the key value
            if self.rightchild:     #if on the rigghtchild of the tree
                self.rightchild.add(value)  #set values to rightchild
        else:
            self.rightchild = binary_tree(value) #values cannot be less then the root key
    ##End of search of our binary tree