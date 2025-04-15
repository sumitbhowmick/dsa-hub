def max_subarray_sum(nums):
    """
    Function to find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Parameters:
    nums (List[int]): List of integers (can include negative numbers).
    
    Returns:
    int: Maximum sum of any contiguous subarray.
    """

    # Edge case: if the input list is empty, return 0
    if not nums:
        return 0

    # Initialize two variables:
    current_sum = nums[0]   # current_sum keeps track of the current subarray sum
    max_sum = nums[0]       # max_sum stores the maximum sum found so far
    start = end = temp_start = 0  # Add index tracking

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        num = nums[i]

        # Start a new subarray at current index if current_sum+num < num else extend the current subarray to include num
        # This is the core of Kadane's algorithm
        if num > current_sum + num:
            current_sum = num
            temp_start = i  # New potential start
        else:
            current_sum += num

        # Update max_sum if the current subarray sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start  # Confirm start index
            end = i             # Confirm end index

    return max_sum, nums[start:end + 1]  # Return sum and subarray


# Example usage:
if __name__ == "__main__":
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = max_subarray_sum(sample_array)
    print(f"Maximum subarray sum is: {max_sum}")
    print(f"Subarray with maximum sum: {subarray}")
