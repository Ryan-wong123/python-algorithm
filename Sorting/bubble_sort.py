def bubbleSort(list, n):
    #start sorting from the first position
    position = 0

    for i in range(n):
        for j in range(i):
            if list[j] > list[j+1]: 
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                position += 1

    #if all values are sorted in the list, return current list
    if (position == 0):
        return list
    else: 
        #else repeat the bubblesort for the list again
        return bubbleSort(list, n)
        
list = [72, 56, 93, 8, 22, 41, 88, 23, 60]
bubbleSort(list, len(list))
print(list) 