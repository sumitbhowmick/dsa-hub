def find_missing_number(nums):
    """
    Finds the missing number from a list containing numbers from 1 to n+1
    with exactly one number missing.

    Args:
    nums (List[int]): List of n unique integers from 1 to n+1 with one missing.

    Returns:
    int: The missing number.
    """
    n = len(nums)   # Since one number is missing
    expected_sum = n * (n + 1) // 2  # Sum of 1 to n
    actual_sum = sum(nums)
    print(f"length: {n}, Expected sum: {expected_sum}, Actual sum: {actual_sum}")
    return expected_sum - actual_sum


nums = [0, 6, 4, 3, 2, 1]  # Missing 3
print("Missing number is:", find_missing_number(nums))