def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                a = list[idx] 
                list[idx] = list[idx + 1]
                list[idx + 1] = a
            
list = [9,8,6,3,7,4,6]
print('List awal : ', list)
bubblesort(list) 
print('Sorted : ', list)