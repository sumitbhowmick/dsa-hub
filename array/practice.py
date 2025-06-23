
def removeDuplicates(nums,k):
    left =0
    right =1
    n = len(nums)

    while(right<n-1):
        if nums[left]==nums[right]:
            right = right+1
        else:
            left+=1
            right+=1
    #return answer

nums = [0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums,5))