def is_palindrome(x):
    """
    Returns True if x is a palindrome integer, False otherwise.
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    # Convert integer to string and compare with its reverse
    return str(x) == str(x)[::-1]

# Example usage:
print(is_palindrome(121))   # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))
