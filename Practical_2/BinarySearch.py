def binary_search(sorted_arr: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if not found."""
    low, high = 0, len(sorted_arr) - 1

    while low <= high:
        # Overflow-safe midpoint calculation in languages with fixed-width ints
        mid = low + (high - low) // 2

        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test driver (input must be sorted)
sorted_nums = [8, 17, 23, 42, 56, 89]
print("Binary found at index:", binary_search(sorted_nums, 56))   # 4
print("Binary missing result:", binary_search(sorted_nums, 15))  # -1
