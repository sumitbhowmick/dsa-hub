#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# # Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

def first_unique_char(s):
    char_dict ={}   #char:[count,first_index]

    # Count occurrences and store first index
    for i, char in enumerate(s):
        if char in char_dict:
            char_dict[char]=[(char_dict[char][0])+1,char_dict[char][1]]
        else:
            char_dict[char] = [1,i]

    #Find first character with count 1
    for char in char_dict:
        if char_dict[char][0]==1:
            return char,char_dict[char][1]
    return -1


print(first_unique_char("ababdce"))