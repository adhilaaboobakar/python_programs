# Q1 : Write a python program that accepts a string and calculates the number of digits and letters.


string=input("Enter a string : ")

ch_count=0
num_count=0

for ch in string:
    if ch.isalpha():
        ch_count+=1
    elif ch.isdigit():
        num_count+=1
print(f"The number of letters= {ch_count}")
print(f"The number of digits= {num_count}")





# Q2 : Write a python program to print multiplication table of a number

# num=int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{i}*{num}={i*num}")





# Q3 : Pattern print

# # 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5


# for row in range(1,6):
#     for coloumn in range(1,row+1):
#         print(row,end="\t")
#     print()



