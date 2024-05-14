# Q1:  Write a Python program to find leap year (user input)

year=int(input("Enter the year "))

if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




# Q2 : Write a python program to sum all the items in the dictionary 

# wc={"apple":200,"orange":40,"grapes":60,"guava":80,"strawbwrry":120}

# total_sum=sum(wc.values())
# print(f"Sum of all items : {total_sum}")







# Q3 : Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *


# for row in range(1,6):
#     for col in range(1,6):
#         print("*",end=" ")
#     print()














# swap first and last elements in a list

# lst=[12,4,8,7,9]

# last=len(lst)
# for num in lst:
#     temp=lst[0]
#     lst[0]=lst[last-1]
#     lst[last-1]=temp
# print(lst)


# find the largest element from the list

# lst=[4,7,3,9,13,5,2]
# larg=lst[0]
# for i in range(0,len(lst)):
#     current=lst[i]
#     if current>larg:
#         larg=current
# print(larg)