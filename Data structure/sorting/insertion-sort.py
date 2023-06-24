def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        j = i-1 
        nxt_element = input_list[i] 
    #compare the current element with next one
    while (input_list[j] > nxt_element) and j >= 0:
        input_list[j+1] = input_list[j] 
        j = j - 1
    input_list[j+1] = nxt_element 

list = [19,2,31,45,30,11,121,27]
insertion_sort(list) 
print(list)