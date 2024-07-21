#time complexity O(n^2)
def SelectionSort(values):
    sortedList = []
    for i in range (0, len(values)):
        indexToMove = IndexOfMin(values)
        #remove the lowest value from the unsorted list and transfer it to the sorted list
        sortedList.append(values.pop(indexToMove))
    return sortedList

def IndexOfMin(values):
    minIndex = 0
    for i in range(1, len(values)):
        if(values[i] < values[minIndex]):
            minIndex = i
    return minIndex

unsortedList = [4,6,1,7,3,9,5,8]
newSortedList = SelectionSort(unsortedList)
print(newSortedList)