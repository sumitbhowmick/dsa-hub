def check_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same backward as forward.
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

print("Palindrome Check for - racecar:", check_palindrome("Racecar"))  # True
print("Palindrome Check for - hello:", check_palindrome("hello"))