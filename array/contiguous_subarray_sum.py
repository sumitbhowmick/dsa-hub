# Given an array of numbers, return true if there is a subarray that sums up to a certain number n. A subarray is a contiguous subset of the array. For example the subarray of [1,2,3,4,5] is [1,2,3] or [3,4,5] or [2,3,4] etc.

# Constraints
# Length of the array <= 100000
# The values in the array will be between 0 and 1000000000
# The target sum n will be between 0 and 1000000000
# The array can be empty
# Expected time complexity : O(n)
# Expected space complexity : O(n)

def subarray(arr,target):
    n = len(arr)
    if n==0:
        return 0
    left=right=0
    temp_sum = 0
    while right<n or left<n:
        #temp_sum = temp_sum+arr[k]
        temp_sum = sum(arr[left:(right+1)])
        print(left, right, temp_sum, target)
        if temp_sum ==target:
            return arr[left:(right+1)]
        elif temp_sum>target:
            left+=1
            #if left>=right:
            #    right=left
        elif right<n:
            right+=1
        elif left<n:
            left+=1
        

    return 0


arr1 = [2,5,12,3,1,9,34,8,4,25,14,2,8,76,21,30,5,3,12]
arr2 = [2,5,10,3,1,9,34,8,4,25,14,2,8,76,21,30,5,3,12]
arr3 = [2,5,10,3,1,9,34,8,25,14,2,8,76,21,30,5,3,1]
arr4 = [2,5,10,3,1,9,4,3,14,2,8,6,21,30,5,3,12]
arr5 = []
target = 12

#print(subarray(arr1,target))
#print(subarray(arr2,target))
#print(subarray(arr3,target))
#print(subarray(arr4,target))
print(subarray(arr5,target))