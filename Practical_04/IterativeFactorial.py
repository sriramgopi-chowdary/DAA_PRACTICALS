def factorial_iterative(n: int) -> int:
    """Compute n! iteratively using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Test driver
for val in [0, 1, 5, 7]:
    print(f"Iterative {val}! = {factorial_iterative(val)}")
