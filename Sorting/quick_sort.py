#selects a pivot and splits the list into half where the numbers lesser than the value of the pivot is on the left hand side
#and the numbers greater than the value of the pivot is on the right hand side
#using the median of three as the pivot is the best case of O(n log n) time complexity
def QuickSort(values):
    if(len(values) <= 1):
        return values
    lessThanPivot = []
    greaterThanPivot = []
    pivot = values[0]

    for value in values[1:]:
        if(value <= pivot):
            lessThanPivot.append(value)
        else:
            greaterThanPivot.append(value)
    return QuickSort(lessThanPivot) + [pivot] + QuickSort(greaterThanPivot)

unsortedList = [8,4,9,6,25,98]
sortedList = QuickSort(unsortedList)
print(sortedList)