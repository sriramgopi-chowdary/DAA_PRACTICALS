def factorial_recursive(n: int) -> int:
    """Compute n! recursively using the relation n! = n * (n - 1)!."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Test driver
for val in [0, 1, 5, 7]:
    print(f"Recursive {val}! = {factorial_recursive(val)}")
