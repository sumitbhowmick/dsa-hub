# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_duplicate(nums):
    i=0
    j=1
    k=len(nums)

    while j<k:
        if nums[i]==nums[j]:
            j+=1
        else:
            i+=1
            nums[i]=nums[j]            
            j+=1

    return i+1

    
nums = [-3,2,2]
print(remove_duplicate(nums), nums)