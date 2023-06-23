def f(n):

    #stop condition 
    if(n==0 or n==1):
        return 1 
    else:
        return n * f(n-1) 
    
n = 3
print(f(n))