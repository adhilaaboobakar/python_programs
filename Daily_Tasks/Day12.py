# Q1: Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number

# sum=0
# while(True):
#     num=int(input("Enter a number"))
#     if num!=0:
#         print(num)
#         sum+=num
        
#     else:
#         print("you entered zero")
#         break

# print(f"Sum of the entered numbers: {sum} ")





# Q2: Write a python program to accept decimal number and display it’s binary number


num=int(input("Enter a number"))
binary=bin(num)
print("binary is",binary)

    









# Q3: Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# for row in range(6,0,-1):
#     for col in range(row):
#         print(row,end=" ")
#     print()