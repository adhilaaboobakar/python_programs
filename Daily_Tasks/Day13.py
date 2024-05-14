# Q1: Write a Python program that Use while loop to display elements from a given list present at odd index positions

# lst=[1,2,3,4,5,6,7]

# i=0
# while(i<len(lst)):
#     if i%2!=0:
#         print(lst[i])
#     i+=1











# Q2: Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

num=int(input("Enter a number"))
square_list = [i**2 for i in range(num, num+10)]
cube_list = [i**3 for i in range(num, num+10)]

print("Square List:", square_list)
print("Cube List:", cube_list)






# Q3: Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1


# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     for col in range(row-1,0,-1):
#         print(col,end=" ")
#     print("")
