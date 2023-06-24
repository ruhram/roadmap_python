def printfun(test) :
    if (test < 1):
        return
    else :
        print(test, end=' ')
        printfun(test - 1)
        print(test, end = ' ')
        return

test = 3 
printfun(test)
