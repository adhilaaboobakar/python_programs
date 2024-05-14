num= int(input("enter a number"))
is_prime= True
i=2
while(i<num):
    if num%i==0:
        is_prime=False
        break
    i+=1
print(is_prime)