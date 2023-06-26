# declare our own string class
class string:

    # magic method to initiate object 
    def __init__(self, string):
        self.string = string 
    
    # print our string project 
    def __repr__(self):
        return 'Object: {}'.format(self.string)

# Driver Code 
if __name__ == '__main__':

    # object creation 
    string1 = string("Hello") 

    # print object location 
    print(string1)