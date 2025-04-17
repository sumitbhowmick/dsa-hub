def two_sum_problem(nums, target):
    """
    Finds two indices in the list such that the numbers at those indices add up to the target.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    num_map ={} #hashmap {num:index}
    answer = [] #list to store the answer

    for i, num in enumerate(nums):
        r = target - num
        if r in num_map:
            #return [num_map[r], i] //if only one solution exists
            answer.append([num_map[r],i])
        num_map[num] = i
    return answer  # Return an empty list if no solution is found

nums = [1, 9, 14, 6, 2, 8, 3, 17, 5, 0, 4, 15]
print(two_sum_problem(nums, 10))