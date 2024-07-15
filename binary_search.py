def binary_search(list, target):
    '''
    binary search requires the list to be sorted first in order to be searched
    binary search breaks list into half first to search  O(log n)
    '''
    first = 0
    last = len(list) - 1

    while (first <= last):
        # the use of // is to divide and round down to the nearest int
        midpoint = (first + last) // 2

        #if the midpoint is the target then just return the value
        if(list[midpoint] == target):
            return midpoint
        #if the value of midpoint is less than the target means the target value is more than the midpoint so the target is in the upper half
        #therefore set the first value as the value after midpoint to get the upper half range
        elif(list[midpoint] < target):
            first = midpoint + 1
        #if the value of midpoint is more than the target means the target value is lesser than the target so the target is in the lower half 
        #therefore set the last value as the value before midpoint to get the lower half range
        else:
            last = midpoint - 1
    
    return None
def verify(index):
    if index is not None:
        print("target found at index", index)
    else:
        print("target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,6)
verify(result)