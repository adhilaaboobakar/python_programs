# Q1: Write a python program to create a list of tuples having first element as the number and second element as the cube of the number




# lst=[ (n,n**3)for n in range(1,11)]
# print(lst)











# Q2: find the length of the string using for loop


# str=input("enter a string : ")

# cout=0
# for ch in str:
#     cout+=1
# print(f"The length of the string: {cout}")






# Q3. Write a program to handling missing keys



# fruits={"apple":200,"orange":50,"grapes":100,"strawberry":250}

# key=input("Enter a fruit : ")

# if key in fruits:
#     print(f"{key} is present")
# else:
#     print(f"{key} is not present")











# Q4.Pattern print 
#         A 
#    B C 
#       D E F 
#      G H I J 
#     K L M N O


a=65
for row in range(1,6):
    for col in range(row,6):
        print(end=" ")
    for col in range(1,row+1):
        print(chr(a),end=" ")

        a+=1

    print()
