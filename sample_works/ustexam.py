

# you have to find the equal or least number from there


# input:6  output :6 reason :1+2+3=6
# input:8  output :6  reason=1+2+3=6 1+2+3+4=10 we want equal or smaller number
# input:10  output :10



def find_least_number(n):
    total = 0
    i = 1
    while total <= n:
        total += i
        if total > n:
            return total - i
        i += 1
    return total

# Test cases
print(find_least_number(6))   # Output: 6 (1+2+3=6)
print(find_least_number(8))   # Output: 6 (1+2+3=6)
print(find_least_number(10))  # Output: 10
