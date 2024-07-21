def insertionSort(list): 
    #decrement from the length of the list to 0 with a decrement value of - 1
    for index in range(len(list) - 1, 0, -1):

        currentvalue = list[index]
        position = index

        #while the current position is not out-of-range of the list and the next number on the position is less than the current position's number
        while position < (len(list)) and list[position - 1] < list[position]:

            #swap the value around so that the higher number ends up at the left side of the list and the smaller number ends up at the right side of the list
            currentvalue = list[position]
            list[position] = list[position - 1]
            list[position - 1] = currentvalue
    
            #increment position by 1
            position = position + 1
    
    
    #since higher number is on the left side of the list and required order is from higher number on the right side, hence reverse the list
    list.reverse()    

list = [72, 56, 93, 8, 22, 41, 88, 23, 60]
insertionSort(list)
print(list) 