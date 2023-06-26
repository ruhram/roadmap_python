#declare our own string class
class string:
    # magic method to initiate object
    def __init__(self, string):
        self.string = string 

#Driver Code 
if __name__ == '__main__':

    # object creationg 
    string1 = string('Hello') 

    # print object location 
    print(string1) 
