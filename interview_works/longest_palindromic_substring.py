def is_palindrome(s):  
    return s == s[::-1]  
def longest_palindrome_naive(s):  
    n = len(s)  
    longest_palindrome = ""  
    # Generate all possible substrings and check if they are palindromes  
    for i in range(n):  
        for j in range(i+1, n):  
            substring = s[i:j]  
            if is_palindrome(substring) and len(substring) > len(longest_palindrome):  
                longest_palindrome = substring  
    return longest_palindrome  
input_str = "baaac"  
print(longest_palindrome_naive(input_str)) 