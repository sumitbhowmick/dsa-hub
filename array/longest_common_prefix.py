#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".


def longest_prefix(strs):
    prefix = ""
    temp_prefix = strs[0]
    for x in strs:

        while(len(temp_prefix)>0):
            if x[:-1]!=temp_prefix:
                temp_prefix=temp_prefix[:-1]
            else:
                break
    return temp_prefix

print(longest_prefix(["flower","flow","flight"]))