

# finding the occurences of a digit in a number


def count_digit(num):
    
    count=0
    while(num!=0):
        digit=num%10
        if digit==2:
            count+=1
            
        num=num//10
    return count
       
print(count_digit(12223))
