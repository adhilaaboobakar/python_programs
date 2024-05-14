# choose a number.if number is odd =num-1
                    # number is even=num/2  until 1
#   print the number of operation to reach 1

def input_num(num):
    count=0
    while(num!=1):
        if num%2==0:
            num=num/2
            count+=1
        elif num%2!=0:
            num=num-1
            count+=1
    return count

print(input_num(15))