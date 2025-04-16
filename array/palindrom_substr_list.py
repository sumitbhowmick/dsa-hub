def all_palindrome_substr(s):
    """
    Find all palindromic substrings in a given string.
    A palindrome is a string that reads the same backward as forward.
    """
    n = len(s)
    palinlist = []

    def expand_around_center(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            palinlist.append(s[l:r+1])
            l -= 1
            r += 1

    for i in range(n):
        l = r = i
        
        # Find odd length palindromes with one in center
        expand_around_center(l, r)
        
        # Find even length palindromes with none in center        
        l = i
        r = l + 1
        expand_around_center(l, r)
        
    palinlist.sort()  # Sort the list to have a consistent order
    print("Palindromic substrings for", s, ":", palinlist)
    return palinlist


all_palindrome_substr("a")
all_palindrome_substr("aa")
all_palindrome_substr("aaa")
all_palindrome_substr("abc")
all_palindrome_substr("abddra")
all_palindrome_substr("abracarb")
all_palindrome_substr("foxxy")