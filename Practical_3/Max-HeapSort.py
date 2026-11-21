def _sift_down(arr: list[int], heap_size: int, root_idx: int) -> None:
    """Restore the max-heap property for the subtree rooted at root_idx."""
    largest = root_idx
    left = 2 * root_idx + 1
    right = 2 * root_idx + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root_idx:
        arr[root_idx], arr[largest] = arr[largest], arr[root_idx]
        _sift_down(arr, heap_size, largest)


def heap_sort(arr: list[int]) -> list[int]:
    """Sort a list in-place in ascending order using max-heap sort."""
    n = len(arr)

    # Step 1: Build max-heap bottom-up from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, n, i)

    # Step 2: Extract max elements one by one from the end
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, end, 0)

    return arr


# Test driver
nums = [42, 17, 89, 23, 56, 8]
print("Original:", nums)
print("Sorted:  ", heap_sort(nums.copy()))
