import random

# Partition function (similar to Lomuto partition scheme)
def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

# Randomized partition for better average performance
def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[high], arr[random_index] = arr[random_index], arr[high]
    return partition(arr, low, high)

# QuickSelect-like algorithm to find the k-th smallest element
def kth_smallest(arr, low, high, k):
    if low <= high:
        # Partition the array and get the pivot index
        pivot_index = randomized_partition(arr, low, high)

        # Position of pivot in the sorted array
        position = pivot_index - low + 1

        if position == k:
            return arr[pivot_index]
        elif k < position:
            return kth_smallest(arr, low, pivot_index - 1, k)
        else:
            return kth_smallest(arr, pivot_index + 1, high, k - position)
    
    return -1  # fallback (should never happen with valid input)


def main():
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    k = int(input("Enter the value of k: "))

    if k < 1 or k > n:
        print(f"Invalid input. k must be between 1 and {n}.")
        return

    result = kth_smallest(arr, 0, n - 1, k)

    suffix = "th"
    if k == 1:
        suffix = "st"
    elif k == 2:
        suffix = "nd"
    elif k == 3:
        suffix = "rd"

    print(f"The {k}{suffix} smallest element is: {result}")

if __name__ == "__main__":
    main()
