# Q1 : Write a python program to find factorial of a prime number

# num=int(input("enter a number "))
# is_prime=True
# fact=1

# for i in range(2,num):
#      if num%i==0:
#         is_prime=False
#         break

# if is_prime:
#         i=1
#         while(i<num+1):
#             fact=fact*i
#             i=i+1
#         print("factorial of",num, "is" , fact)
# else:
#      print(num,"is not prime")







# Q2 :Write a python program to display Fibinacco series and specify that number even or oddprint(0)
 
previous_num=0
current_num=1

print(previous_num)

for i in range(1,11):
    next=previous_num+current_num
    if next%2==0:
        print(next,"is even")
    else:
        print(next,"is odd")
    previous_num=current_num
    current_num=next
   







# Q3 : Write a python program to reverse digits in a number

# num=int(input("Enter a number "))
# while(num!=0):
#     last_digit=num%10 #
#     print(last_digit,end="")
#     num=num//10



