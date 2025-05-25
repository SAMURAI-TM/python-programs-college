def is_palindrome(num):
    num_str = str(num)
    
    def helper(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return helper(s[1:-1])
    
    return helper(num_str)

# Example usage
number = int(input("Enter the number:"))
print(is_palindrome(number))  # Output: True
