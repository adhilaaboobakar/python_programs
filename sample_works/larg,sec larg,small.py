

# second largest among 3 numbers

def second_largest(n1,n2,n3):

    if(n1>n2 and n1<n3 or n1>n3 and n1<n2):
        print(n1," is second_largest")
    elif(n2>n3 and n2<n1 or n2>n1 and n2<n3):
        print(n2,"is second largerst")
    elif(n3>n1 and n3<n2 or n3>n2 and n3<n1):
        print(n3,"is second largest")
    
print(second_largest(6,7,8))