

# Arrange string characters such that lowercase letters should come first

# str1 = PyNaTive
# output : yaivePNT



def lower_case(str1):
    
    
    s2=""
    s3=""
    res=""
    for ch in str1:
        if ch.islower():
            s2+=ch
        else:
            s3+=ch
        res=s2+s3

    return res

print(lower_case("PyNaTive"))







# Count all letters, digits, and special symbols from a given string


# Total counts of chars, digits, and symbols 

# Chars = 8 
# Digits = 3 
# Symbol = 4



text="abcRGt6784%$^&3y"


def count_str(text):

    alpha_count=0
    dig_count=0
    symb_count=0

    for ch in text:
        if ch.isalpha():
            alpha_count+=1
        elif ch.isdigit():
            dig_count+=1
        else:
            symb_count+=1

    return alpha_count,dig_count,symb_count
    
print(count_str("abc34%^&239uj"))