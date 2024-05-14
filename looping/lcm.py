# print lcm of 2 numbers

n1=int(input("enter num1 "))
n2 = int(input("enter num2 "))

sm_num = n1 if n1<n2 else n2
i=1
while(i<=sm_num):
    if n1%i ==0 and n2%i==0:
        gcd=i
    i+=1
print(gcd)

lcm=(n1*n2/gcd)
print(lcm)