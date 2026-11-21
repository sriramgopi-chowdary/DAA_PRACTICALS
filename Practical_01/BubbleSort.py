def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Stop early if no swaps occurred in a full pass
        if not swapped:
            break
    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(numbers))
