def linear_search(arr: list[int], target: int) -> int:
    """Return the index of target in arr, or -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Test driver
nums = [42, 17, 89, 23, 56, 8]
print("Linear found at index:", linear_search(nums, 23))   # 3
print("Linear missing result:", linear_search(nums, 100))  # -1
