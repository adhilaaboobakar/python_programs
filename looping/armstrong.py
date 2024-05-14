# input a number and print the sum 


num= input("enter a number")
digit_count =len(num)
num= int(num)
orginal=num
sum=0
while(num!=0):
     digit=num%10
     exp= digit**digit_count
     sum+= exp
     num = num//10

if sum==orginal:
     print("armstrong")
else:
     print("not armstrong")

# print(f"{orginal}" is armstrong" number if sum==orginal else" not armstrong")