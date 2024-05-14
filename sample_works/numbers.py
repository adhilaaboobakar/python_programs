

# check prime number


def prime(num):
    for i in range(2,num):
        if num%i==0:
            result="not prime"
        else:
            result="prime"

    return result
print(prime(7))


# factorial of a number

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

print(fact(4))


# palindrome number

def is_palindrome(num):

    while(num!=0):
        digit=num%10
        num=num//10






# armstrong number


def is_armstrong(num):
    # Count the number of digits
    num_str = str(num)
    digit_count = len(num_str)
    
    # Convert the number to an integer
    num = int(num)
    original = num
    armstrong_sum = 0
    
    # Calculate the sum of each digit raised to the power of digit_count
    while num != 0:
        digit = num % 10
        exp = digit ** digit_count
        armstrong_sum += exp
        num = num // 10
    
    # Check if the sum is equal to the original number
    if armstrong_sum == original:
        result=True
    else:
        result= False
    return result

print(is_armstrong(153))
