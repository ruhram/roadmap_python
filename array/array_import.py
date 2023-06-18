import array as arr  

values = arr.array('i',[10,20,30])

#prints each individual value in the array
print(values)

for value in range(len(values)):
    print(values[value])