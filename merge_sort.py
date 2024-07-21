#sorts the list in ascending order in O(n log n) time complexity
def Merge_Sort(list):
    if(len(list) <= 1):
        return list
    
    leftHalf, rightHalf = Split(list)
    left = Merge_Sort(leftHalf)
    right = Merge_Sort(rightHalf)

    return Merge(left,right)

#divide the list at mid point into sublists and return 2 sublists - left and right with O(log n) time complexity
def Split(list):
    #get the middle point rounded down to nearst int
    mid = len(list)//2
    #assign the first half and second half into 2 separate lists
    left = list[:mid]
    right = list[mid:]

    return left,right

#merge the 2 sublists and sort in ascending order with O(n) time complexity
def Merge(left,right):
    newList = []

    leftListIndex = 0
    rightListIndex = 0

    #if the length of both list are equal
    while leftListIndex<len(left) and rightListIndex < len(right):
        if(left[leftListIndex] < right[rightListIndex]):
            newList.append(left[leftListIndex])
            leftListIndex += 1
        else:
            newList.append(right[rightListIndex])
            rightListIndex += 1

    #if the length of left list is greater than right list
    while leftListIndex < len(left):
        newList.append(left[leftListIndex])
        leftListIndex += 1

    #if the length of the left list is lesser than the right list
    while rightListIndex < len(right):
        newList.append(right[rightListIndex])
        rightListIndex += 1

    return newList


def VerifySorted(list):
    lengthOfList = len(list)
    if(lengthOfList == 0 or lengthOfList == 1):
        return True
    
    return list[0] < list[1] and VerifySorted(list[1:])


unsortedList = [4,8,2,76,654,9,543,65,34]
sortedList = Merge_Sort(unsortedList)
print(str(sortedList) + "is sorted correctly "+ str(VerifySorted(sortedList)))