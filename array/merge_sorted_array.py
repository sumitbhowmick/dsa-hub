# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge_sorted_array(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 in-place, assuming nums1 has size m + n.
    
    Args:
    nums1 (List[int]): First list with m meaningful elements followed by n zeroes.
    m (int): Number of valid elements in nums1.
    nums2 (List[int]): Second list with n elements.
    n (int): Number of elements in nums2.
    """
    # Start filling from the end
    i = m - 1  # Pointer for last valid element in nums1
    j = n - 1  # Pointer for last element in nums2
    k = m + n - 1  # Pointer for last position in nums1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If nums2 still has elements, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge_sorted_array(nums1,3,nums2, 3)
print(nums1) # Expected output: [1,2,2,3,5,6]