
def findDuplicates(nums):
    freqmap = {}
    answer =[]

    for num in nums:
        freqmap[num] = freqmap.get(num, 0)+1
    
    for i,count in freqmap.items():
        if count>1:
            answer.append(i)
    return answer

nums = [1, 1, 2, 3, 3, 6, 3, 6, 1, 8]
print(findDuplicates(nums))