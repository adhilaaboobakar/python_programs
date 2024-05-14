# def palindrome_check(input):
#     reversed_str=""

#     for char in input:
#         reversed_str=char+reversed_str
#     if reversed_str==input:
#         return "string is a palindrome"
#     else:
#         return "string is not a palindrome"

# my_str=input("enter a string : ")  
# print(palindrome_check(my_str))


def palindrome_check(input):
    reversed_str=input[::-1]
    if input==reversed_str:
        return True
    else:
        return False
    
print(palindrome_check("malayalam"))
